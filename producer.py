"""
WillowLoop producer.py
Downloads a nature video clip from Pixabay/Pexels,
loops it to 2 hours via FFmpeg concat+copy,
and cuts a 59-second Short.
"""
import os
import json
import math
import logging
import subprocess
import requests
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

PIXABAY_KEY = os.environ.get("PIXABAY_KEY", "")
PEXELS_KEY = os.environ.get("PEXELS_KEY", "")
WORK_DIR = "/tmp/willowloop"


# ─── Helpers ──────────────────────────────────────────────────────────────────

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)
    return path


def get_duration(path):
    """Return duration in seconds using ffprobe."""
    cmd = [
        "ffprobe", "-v", "quiet",
        "-print_format", "json",
        "-show_format", path,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    data = json.loads(result.stdout)
    return float(data["format"]["duration"])


def download_file(url, dest, label="file"):
    """Stream-download a file. Returns True on success."""
    logger.info(f"Downloading {label} ...")
    headers = {}
    if "pexels.com" in url and PEXELS_KEY:
        headers["Authorization"] = PEXELS_KEY
    try:
        with requests.get(url, headers=headers, stream=True, timeout=180) as r:
            r.raise_for_status()
            size = 0
            with open(dest, "wb") as f:
                for chunk in r.iter_content(chunk_size=2 * 1024 * 1024):
                    if chunk:
                        f.write(chunk)
                        size += len(chunk)
        logger.info(f"  -> {size / 1024 / 1024:.1f} MB saved to {dest}")
        return True
    except Exception as e:
        logger.warning(f"Download failed ({label}): {e}")
        if os.path.exists(dest):
            os.remove(dest)
        return False


# ─── Video search ─────────────────────────────────────────────────────────────

def search_pixabay_video(queries, min_duration=20, min_width=1280):
    """Return list of Pixabay video hits sorted by duration desc."""
    results = []
    seen = set()
    for query in queries:
        try:
            r = requests.get(
                "https://pixabay.com/api/videos/",
                params={
                    "key": PIXABAY_KEY,
                    "q": query,
                    "video_type": "film",
                    "per_page": 20,
                    "safesearch": "true",
                    "min_width": min_width,
                },
                timeout=30,
            )
            r.raise_for_status()
            for hit in r.json().get("hits", []):
                if hit["id"] in seen:
                    continue
                dur = hit.get("duration", 0)
                if dur < min_duration:
                    continue
                videos = hit.get("videos", {})
                url = width = None
                for q in ("large", "medium", "small"):
                    v = videos.get(q, {})
                    if v.get("url"):
                        url = v["url"]
                        width = v.get("width", 0)
                        break
                if not url:
                    continue
                results.append({"id": hit["id"], "url": url, "duration": dur,
                                 "width": width, "source": "pixabay"})
                seen.add(hit["id"])
        except Exception as e:
            logger.warning(f"Pixabay search '{query}': {e}")
    results.sort(key=lambda x: x["duration"], reverse=True)
    return results


def search_pexels_video(queries, min_duration=20):
    """Fallback: search Pexels for video clips."""
    if not PEXELS_KEY:
        return []
    results = []
    seen = set()
    headers = {"Authorization": PEXELS_KEY}
    for query in queries:
        try:
            r = requests.get(
                "https://api.pexels.com/videos/search",
                headers=headers,
                params={"query": query, "per_page": 10, "min_duration": min_duration},
                timeout=30,
            )
            r.raise_for_status()
            for vid in r.json().get("videos", []):
                if vid["id"] in seen:
                    continue
                dur = vid.get("duration", 0)
                if dur < min_duration:
                    continue
                files = sorted(vid.get("video_files", []),
                               key=lambda f: f.get("width", 0), reverse=True)
                if not files:
                    continue
                f = files[0]
                results.append({"id": vid["id"], "url": f["link"], "duration": dur,
                                 "width": f.get("width", 0), "source": "pexels"})
                seen.add(vid["id"])
        except Exception as e:
            logger.warning(f"Pexels search '{query}': {e}")
    results.sort(key=lambda x: x["duration"], reverse=True)
    return results


# ─── FFmpeg helpers ───────────────────────────────────────────────────────────

def _run_ffmpeg(cmd):
    """Run an ffmpeg command; raise on failure with last 800 chars of stderr."""
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"FFmpeg failed:\n{result.stderr[-800:]}")
    return result


def normalize_clip(src, dest):
    """
    Re-encode the source clip to a clean h264/aac baseline so concat-copy works
    reliably. Keeps 720p max, ultrafast preset = very fast.
    """
    logger.info("Normalizing clip for clean looping ...")
    _run_ffmpeg([
        "ffmpeg", "-y", "-i", src,
        "-vf", "scale='min(1280,iw)':'min(720,ih)':force_original_aspect_ratio=decrease",
        "-c:v", "libx264", "-preset", "ultrafast", "-crf", "26",
        "-c:a", "aac", "-b:a", "128k",
        "-movflags", "+faststart",
        dest,
    ])
    logger.info(f"Normalized clip: {dest}")


def create_loop_video(clip_path, output_path, duration=7200):
    """
    Concat-copy the clip N times to fill `duration` seconds.
    Uses -c:v copy + -c:a copy for speed (no re-encode).
    """
    clip_dur = get_duration(clip_path)
    n_reps = math.ceil(duration / clip_dur) + 3

    concat_file = clip_path + ".concat.txt"
    abs_clip = os.path.abspath(clip_path)
    with open(concat_file, "w") as f:
        for _ in range(n_reps):
            f.write(f"file '{abs_clip}'\n")

    logger.info(f"Looping {clip_dur:.0f}s clip x{n_reps} -> {duration // 3600}h video ...")
    try:
        _run_ffmpeg([
            "ffmpeg", "-y",
            "-f", "concat", "-safe", "0", "-i", concat_file,
            "-t", str(duration),
            "-c:v", "copy", "-c:a", "copy",
            output_path,
        ])
    except RuntimeError:
        logger.warning("Copy-mode failed, falling back to re-encode ...")
        _run_ffmpeg([
            "ffmpeg", "-y",
            "-f", "concat", "-safe", "0", "-i", concat_file,
            "-t", str(duration),
            "-c:v", "libx264", "-preset", "ultrafast", "-crf", "28",
            "-c:a", "aac", "-b:a", "128k",
            output_path,
        ])
    finally:
        if os.path.exists(concat_file):
            os.remove(concat_file)

    logger.info(f"Loop video ready: {output_path}")


def create_short(main_video_path, output_path, duration=59):
    """
    Cut the first `duration` seconds and crop to 9:16 vertical for YouTube Shorts.
    Falls back to a plain cut if the crop fails.
    """
    logger.info(f"Creating {duration}s Short ...")
    try:
        _run_ffmpeg([
            "ffmpeg", "-y",
            "-i", main_video_path,
            "-t", str(duration),
            "-vf", "crop=ih*9/16:ih,scale=1080:1920",
            "-c:v", "libx264", "-preset", "fast", "-crf", "23",
            "-c:a", "aac", "-b:a", "128k",
            output_path,
        ])
    except RuntimeError:
        logger.warning("Vertical crop failed; using plain cut for Short.")
        _run_ffmpeg([
            "ffmpeg", "-y",
            "-i", main_video_path,
            "-t", str(duration),
            "-c:v", "copy", "-c:a", "copy",
            output_path,
        ])
    logger.info(f"Short ready: {output_path}")


# ─── Main produce function ────────────────────────────────────────────────────

def produce(topic):
    """
    Download a clip, normalize it, loop to 2h, cut a Short.
    Returns (main_video_path, short_path, metadata_dict).
    """
    ensure_dir(WORK_DIR)
    slug = topic["slug"]
    today = datetime.now(timezone.utc).strftime("%Y%m%d")

    # 1. Find video clips
    logger.info(f"[{topic['name']}] Searching Pixabay ...")
    clips = search_pixabay_video(topic["video_queries"])
    if not clips:
        logger.info("Pixabay empty -> trying Pexels ...")
        clips = search_pexels_video(topic["video_queries"])
    if not clips:
        raise RuntimeError(f"No video clips found for topic: {topic['name']}")

    # 2. Download best clip (try up to 3)
    raw_clip = os.path.join(WORK_DIR, f"{slug}_raw_{today}.mp4")
    downloaded = False
    for clip_info in clips[:3]:
        logger.info(f"Trying clip {clip_info['id']} ({clip_info['duration']}s, {clip_info['source']}) ...")
        if download_file(clip_info["url"], raw_clip, f"{topic['name']} clip"):
            downloaded = True
            break
    if not downloaded:
        raise RuntimeError("Could not download any video clip.")

    # 3. Normalize clip
    norm_clip = os.path.join(WORK_DIR, f"{slug}_norm_{today}.mp4")
    normalize_clip(raw_clip, norm_clip)
    os.remove(raw_clip)

    # 4. Create 2-hour loop
    main_path = os.path.join(WORK_DIR, f"{slug}_main_{today}.mp4")
    create_loop_video(norm_clip, main_path, topic["duration"])
    os.remove(norm_clip)

    # 5. Create Short
    short_path = os.path.join(WORK_DIR, f"{slug}_short_{today}.mp4")
    create_short(main_path, short_path, duration=59)

    # 6. Build metadata
    metadata = {
        "main": {
            "title": topic["title"],
            "description": topic["description"],
            "tags": topic["tags"],
            "category_id": topic["category_id"],
            "privacy": "public",
        },
        "short": {
            "title": topic["short_title"],
            "description": topic["short_description"],
            "tags": topic["tags"],
            "category_id": topic["category_id"],
            "privacy": "public",
        },
    }
    return main_path, short_path, metadata
