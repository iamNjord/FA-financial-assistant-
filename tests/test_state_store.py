from bot.state.store import StateStore


def test_state_store(tmp_path):
    db = tmp_path / "state.db"
    s = StateStore(db)
    s.set_prev_smoothed("THYAO.IS", 77)
    assert s.get_prev_smoothed("THYAO.IS") == 77
    assert s.report_changed("daily", "abc") is True
    assert s.report_changed("daily", "abc") is False
