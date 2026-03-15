import pandas as pd
import pandas_ta as ta


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["rsi14"] = ta.rsi(out["close"], length=14)
    out["atr14"] = ta.atr(out["high"], out["low"], out["close"], length=14)
    out["sma20"] = ta.sma(out["close"], length=20)
    out["sma50"] = ta.sma(out["close"], length=50)
    out["macd_hist"] = ta.macd(out["close"]).iloc[:, 2]
    return out
