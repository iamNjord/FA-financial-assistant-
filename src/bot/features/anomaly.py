import pandas as pd


def anomaly_flags(df: pd.DataFrame) -> dict[str, bool]:
    r1d = df["close"].pct_change().iloc[-1]
    gap = (df["open"].iloc[-1] / df["close"].iloc[-2]) - 1
    return {
        "R1D_OUTLIER": abs(r1d) > 0.15,
        "GAP_OUTLIER": abs(gap) > 0.10,
        "LOW_LIQUIDITY": (df["close"].mul(df["volume"]).rolling(20).mean().iloc[-1] < 20_000_000),
    }
