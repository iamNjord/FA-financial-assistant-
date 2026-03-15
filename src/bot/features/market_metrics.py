import pandas as pd


def relative_strength(df_symbol: pd.DataFrame, df_bench: pd.DataFrame) -> tuple[float, float]:
    rs20 = (df_symbol["close"].iloc[-1] / df_symbol["close"].iloc[-20]) / (df_bench["close"].iloc[-1] / df_bench["close"].iloc[-20])
    rs5 = (df_symbol["close"].iloc[-1] / df_symbol["close"].iloc[-5]) / (df_bench["close"].iloc[-1] / df_bench["close"].iloc[-5])
    return float(rs20), float(rs5)
