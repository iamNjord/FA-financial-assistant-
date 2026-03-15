from pathlib import Path
import pandas as pd


def write_report(df: pd.DataFrame, path: str) -> Path:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(p, index=False)
    return p
