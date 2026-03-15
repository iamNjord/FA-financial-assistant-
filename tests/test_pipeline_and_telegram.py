from bot.strategies.daily_scan import make_daily_signal
from bot.notifications.telegram import send_telegram_message


def test_pipeline_mock_and_telegram_stub(caplog):
    caplog.set_level("INFO")
    sig = make_daily_signal("THYAO.IS", 80, True)
    assert sig.action == "BUY"
    send_telegram_message("", "", "hello")
    assert "Telegram disabled" in caplog.text
