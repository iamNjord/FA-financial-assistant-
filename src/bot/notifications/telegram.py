import logging

logger = logging.getLogger(__name__)


def send_telegram_message(token: str, chat_id: str, text: str) -> None:
    if not token or not chat_id:
        logger.info("Telegram disabled: missing token/chat_id")
        return
    logger.info("Telegram message queued: %s", text[:80])
