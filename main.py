#!/usr/bin/env python3
"""
WillowLoop main.py
Daily orchestrator: pick topic -> produce -> upload -> report.
"""
import sys
import logging
import traceback
from datetime import datetime, timezone

from topics import TOPICS
from producer import produce
from uploader import get_youtube_service, upload_video, get_channel_stats
from notifier import send_telegram_report

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)


def pick_topic():
    """Cycle through topics sequentially, tracking progress in state.json."""
    import json, os
    state_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "state.json")
    try:
        with open(state_path) as f:
            state = json.load(f)
        idx = state.get("topic_index", 0)
    except FileNotFoundError:
        doy = datetime.now(timezone.utc).timetuple().tm_yday
        idx = doy % len(TOPICS)
    topic = TOPICS[idx % len(TOPICS)]
    with open(state_path, "w") as f:
        json.dump({"topic_index": idx + 1}, f)
    return topic


def main():
    start = datetime.now(timezone.utc)
    logger.info("=" * 60)
    logger.info("\U0001f33f WillowLoop â Daily Run Starting")
    logger.info(f"   {start.strftime('%Y-%m-%d %H:%M UTC')}")
    logger.info("=" * 60)

    result = {
        "success":   False,
        "topic":     None,
        "main_url":  None,
        "short_url": None,
        "error":     None,
    }
    channel_stats = None

    try:
        topic = pick_topic()
        result["topic"] = topic["name"]
        logger.info(f"Today's topic: {topic['emoji']} {topic['name']}")

        # Produce videos
        main_path, short_path, metadata = produce(topic)

        # Upload
        youtube = get_youtube_service()

        logger.info("Uploading main video ...")
        main_id = upload_video(youtube, main_path, metadata["main"], is_short=False)
        result["main_url"] = f"https://youtu.be/{main_id}"

        logger.info("Uploading Short ...")
        short_id = upload_video(youtube, short_path, metadata["short"], is_short=True)
        result["short_url"] = f"https://youtu.be/{short_id}"

        result["success"] = True

        # Fetch channel stats for the report
        logger.info("Fetching channel stats ...")
        channel_stats = get_channel_stats(youtube, video_id=main_id)

        logger.info("â All done!")

    except Exception as exc:
        result["error"] = str(exc)
        logger.error(f"Fatal error: {exc}")
        logger.error(traceback.format_exc())

    # Send Telegram report
    elapsed_min = (datetime.now(timezone.utc) - start).seconds // 60
    try:
        send_telegram_report(result, elapsed_min, channel_stats)
    except Exception as e:
        logger.warning(f"Telegram report failed: {e}")

    return 0 if result["success"] else 1


if __name__ == "__main__":
    sys.exit(main())
