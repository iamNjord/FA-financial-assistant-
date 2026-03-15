import pandas as pd


def weekly_mon_fri_returns(df: pd.DataFrame) -> pd.DataFrame:
    d = df.copy()
    d["week"] = d.index.to_period("W")
    out = d.groupby("week").agg(mon_open=("open", "first"), fri_close=("close", "last"))
    out["ret"] = out["fri_close"] / out["mon_open"] - 1
    return out
