import json
import pandas as pd
from pathlib import Path


def normalize_symbol(symbol: str, use_is_suffix: bool = True) -> str:
    s = symbol.strip().upper()
    if use_is_suffix and not s.endswith(".IS"):
        return f"{s}.IS"
    return s.replace(".IS", "") if not use_is_suffix else s


def load_universe(source: str, path: str, use_is_suffix: bool = True, watchlist: list[str] | None = None) -> list[str]:
    if source == "watchlist":
        raw = watchlist or []
    else:
        p = Path(path)
        if source == "csv":
            df = pd.read_csv(p)
            raw = df["symbol"].tolist()
        elif source == "json":
            raw = json.loads(p.read_text())["symbols"]
        else:
            raise ValueError("Unsupported universe source")
    return [normalize_symbol(s, use_is_suffix) for s in raw]
