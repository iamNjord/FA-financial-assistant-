import pandas as pd
from bot.features.regime import detect_regime, regime_multiplier
from bot.features.market_metrics import relative_strength


def test_regime_and_rs():
    close = pd.Series(range(1, 260))
    df = pd.DataFrame({"close": close})
    assert detect_regime(df) == "BULL"
    assert regime_multiplier("BEAR") == 0.70
    rs20, rs5 = relative_strength(df, df)
    assert rs20 == 1.0 and rs5 == 1.0
