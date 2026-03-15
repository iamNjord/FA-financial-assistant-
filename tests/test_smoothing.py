from bot.features.smoothing import smooth_score, hysteresis_pass


def test_smoothing_and_hysteresis():
    assert smooth_score(60, 50) == 57
    assert hysteresis_pass(50, 59, threshold=8) is True
    assert hysteresis_pass(50, 55, threshold=8) is False
