"""
WillowLoop notifier.py
Sends a daily run report to Telegram.
"""
import os
import logging
import requests
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("TELEGRAM_TOKEN", "")
CHAT_ID   = os.environ.get("TELEGRAM_CHAT_ID", "")

def send_telegram_report(result: dict, duration_min: int, channel_stats: dict = None):
    """
    Send a run summary to the Telegram bot.
    result keys: success, topic, main_url, short_url, error
    channel_stats keys: subscribers, views, videos (or None)
    """
    if not BOT_TOKEN or not CHAT_ID:
        logger.warning("Telegram env vars not set; skipping notification.")
        return

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    if result["success"]:
        lines = [
            "✅ <b>WillowLoop</b> — Daily Run Complete",
            f"U0001f4c5 {now}",
            "",
            f"U0001f3af Topic: {result['topic']}",
            "",
            f"U0001f4f9 Main Video: {result.get('main_url', 'N/A')}",
            f"▶️ Short: {result.get('short_url', 'N/A')}",
        ]
        if channel_stats:
            lines += [
                "",
                "U0001f4ca <b>Channel Stats:</b>",
                f"U0001f465 Subscribers: {channel_stats.get('subscribers', '–')}",
                f"U0001f441 Total Views: {channel_stats.get('views', '–')}",
                f"U0001f3ac Total Videos: {channel_stats.get('videos', '–')}",
            ]
    else:
        lines = [
            "❌ <b>WillowLoop</b> — Run FAILED",
            f"U0001f4c5 {now}",
            "",
            f"U0001f3af Topic: {result.get('topic', 'unknown')}",
            f"⏱ Duration: {duration_min} min",
            f"U0001f41b Error: <code>{result.get('error', 'unknown')[:300]}</code>",
        ]

    text = "\n".join(lines)
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        resp = requests.post(
            url,
            json={"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"},
            timeout=15,
        )
        if not resp.ok:
            logger.warning(f"Telegram API error {resp.status_code}: {resp.text[:300]}")
        else:
            logger.info("Telegram report sent.")
    except Exception as e:
        logger.warning(f"Telegram send failed: {e}")
