import pandas as pd


def detect_regime(df: pd.DataFrame) -> str:
    sma50 = df["close"].rolling(50).mean().iloc[-1]
    sma200 = df["close"].rolling(200).mean().iloc[-1]
    price = df["close"].iloc[-1]
    if price > sma50 > sma200:
        return "BULL"
    if price < sma50 < sma200:
        return "BEAR"
    return "NEUTRAL"


def regime_multiplier(regime: str) -> float:
    return {"BULL": 1.0, "NEUTRAL": 0.85, "BEAR": 0.70}.get(regime, 0.85)
