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
    """Pick next unused topic from shuffled pool. Never repeats until all topics are used."""
    import json as _json, os as _os, random as _random
    from topics import TOPICS
    state_path = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "state.json")
    try:
        with open(state_path) as _f:
            _state = _json.load(_f)
        _pool = [i for i in _state.get("pool", []) if i < len(TOPICS)]
    except FileNotFoundError:
        _pool = []
    if not _pool:
        _pool = list(range(len(TOPICS)))
        _random.shuffle(_pool)
    _idx = _pool.pop(0)
    topic = TOPICS[_idx]
    with open(state_path, "w") as _f:
        _json.dump({"pool": _pool}, _f)
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
        main_id, channel_id = upload_video(youtube, main_path, metadata["main"], is_short=False)
        result["main_url"] = f"https://youtu.be/{main_id}"

        logger.info("Uploading Short ...")
        short_id, _ = upload_video(youtube, short_path, metadata["short"], is_short=True)
        result["short_url"] = f"https://youtu.be/{short_id}"

        result["success"] = True

        # Fetch channel stats for the report
        logger.info("Fetching channel stats ...")
        channel_stats = get_channel_stats(youtube, video_id=main_id, channel_id=channel_id)

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
