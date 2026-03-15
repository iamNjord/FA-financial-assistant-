from bot.scoring.formulas import entry_score, risk_score, composite_score


def test_scoring_formulas():
    e = entry_score(80, 80, 80, 80, 80)
    r = risk_score(50, 50, 50, 50, 50)
    c = composite_score(e, r)
    assert e <= 100
    assert r <= 100
    assert c < e
