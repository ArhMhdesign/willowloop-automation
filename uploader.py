"""
WillowLoop uploader.py
Authenticates with YouTube via OAuth2 refresh token and uploads videos.
"""
import os
import time
import logging
from pathlib import Path

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

logger = logging.getLogger(__name__)

MAX_RETRIES = 5
RETRIABLE_STATUS_CODES = {500, 502, 503, 504}


def get_youtube_service():
    """Build YouTube API client using env-var credentials."""
    creds = Credentials(
        token=None,
        refresh_token=os.environ['YT_REFRESH_TOKEN'],
        client_id=os.environ['YT_CLIENT_ID'],
        client_secret=os.environ['YT_CLIENT_SECRET'],
        token_uri='https://oauth2.googleapis.com/token',
    )
    creds.refresh(Request())
    return build('youtube', 'v3', credentials=creds)


def upload_video(youtube, file_path, meta, is_short=False):
    """
    Upload a video file to YouTube.
    meta keys: title, description, tags, category_id, privacy
    Returns the video ID string.
    """
    title = meta["title"]
    if is_short and "#shorts" not in title.lower():
        title = title + " #Shorts"

    body = {
        "snippet": {
            "title": title[:100],
            "description": meta["description"][:5000],
            "tags": meta.get("tags", [])[:500],
            "categoryId": meta.get("category_id", "22"),
        },
        "status": {
            "privacyStatus": meta.get("privacy", "public"),
            "selfDeclaredMadeForKids": False,
        },
    }

    file_size_mb = Path(file_path).stat().st_size / 1024 / 1024
    logger.info(f"Uploading: {title[:60]} ({file_size_mb:.0f} MB)")

    media = MediaFileUpload(
        file_path,
        mimetype="video/mp4",
        resumable=True,
        chunksize=10 * 1024 * 1024,
    )
    request = youtube.videos().insert(
        part=",".join(body.keys()),
        body=body,
        media_body=media,
    )

    response = None
    retries = 0
    while response is None:
        try:
            status, response = request.next_chunk()
            if status:
                pct = int(status.progress() * 100)
                if pct % 20 == 0:
                    logger.info(f"  Upload progress: {pct}%")
        except HttpError as e:
            if e.resp.status in RETRIABLE_STATUS_CODES:
                retries += 1
                if retries > MAX_RETRIES:
                    raise RuntimeError(f"Upload failed after {MAX_RETRIES} retries: {e}")
                wait = 2 ** retries
                logger.warning(f"Retriable error {e.resp.status}; retrying in {wait}s …")
                time.sleep(wait)
            else:
                raise

    video_id = response["id"]
    logger.info(f"Upload complete → https://youtu.be/{video_id}")
    return video_id
