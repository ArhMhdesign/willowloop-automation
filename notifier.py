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
            "\u2705 <b>WillowLoop</b> \u2014 Daily Run Complete",
            f"📅 {now}",
            "",
            f"🎯 Topic: {result['topic']}",
            "",
            f"📹 Main Video: {result.get('main_url', 'N/A')}",
            f"\u25b6\ufe0f Short: {result.get('short_url', 'N/A')}",
        ]
        if channel_stats:
            lines += [
                "",
                "📊 <b>Channel Stats:</b>",
                f"👥 Subscribers: {channel_stats.get('subscribers', '\u2013')}",
                f"👁 Total Views: {channel_stats.get('views', '\u2013')}",
                f"🎬 Total Videos: {channel_stats.get('videos', '\u2013')}",
            ]
    else:
        lines = [
            "\u274c <b>WillowLoop</b> \u2014 Run FAILED",
            f"📅 {now}",
            "",
            f"🎯 Topic: {result.get('topic', 'unknown')}",
            f"\u23f1 Duration: {duration_min} min",
            f"🐛 Error: <code>{result.get('error', 'unknown')[:300]}</code>",
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
