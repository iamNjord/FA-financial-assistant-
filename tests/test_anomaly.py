import pandas as pd
from bot.features.anomaly import anomaly_flags


def test_anomaly_rules():
    df = pd.DataFrame({
        "open": [100, 130],
        "close": [100, 116],
        "volume": [1_000_000, 1_000_000],
    })
    flags = anomaly_flags(df)
    assert flags["GAP_OUTLIER"]
