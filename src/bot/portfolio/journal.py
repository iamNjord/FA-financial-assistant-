from pathlib import Path
import pandas as pd


def write_trade_journal(trades: list[dict], path: str) -> Path:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(trades).to_csv(p, index=False)
    return p
