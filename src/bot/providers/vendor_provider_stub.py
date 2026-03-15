import pandas as pd
from .base import DataProvider


class VendorProviderStub(DataProvider):
    def fetch_ohlcv(self, symbol: str, interval: str = "1d", lookback: str = "1y") -> pd.DataFrame:
        return pd.DataFrame(columns=["open", "high", "low", "close", "volume"])
