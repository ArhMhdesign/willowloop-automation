"""
WillowLoop notifier.py
Sends a daily run report to Telegram.
"""
import os
import logging
import requests

logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")


def send_telegram_report(result: dict, duration_min: int):
    """
    Send a run summary to the Telegram bot.
    result keys: success, topic, main_url, short_url, error
    """
    if not BOT_TOKEN or not CHAT_ID:
        logger.warning("Telegram env vars not set; skipping notification.")
        return

    if result["success"]:
        icon = "✅"
        lines = [
            f"{icon} *WillowLoop* — Daily Run Complete",
            f"🎯 Topic: {result['topic']}",
            f"⏱ Duration: {duration_min} min",
            f"📹 Main video: {result.get('main_url', 'N/A')}",
            f"▶️ Short: {result.get('short_url', 'N/A')}",
        ]
    else:
        icon = "❌"
        lines = [
            f"{icon} *WillowLoop* — Run FAILED",
            f"🎯 Topic: {result.get('topic', 'unknown')}",
            f"⏱ Duration: {duration_min} min",
            f"🐛 Error: `{result.get('error', 'unknown')}`",
        ]

    text = "\n".join(lines)
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        resp = requests.post(
            url,
            json={"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"},
            timeout=15,
        )
        resp.raise_for_status()
        logger.info("Telegram report sent.")
    except Exception as e:
        logger.warning(f"Telegram send failed: {e}")
