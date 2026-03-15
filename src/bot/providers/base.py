from abc import ABC, abstractmethod
import pandas as pd


class DataProvider(ABC):
    @abstractmethod
    def fetch_ohlcv(self, symbol: str, interval: str = "1d", lookback: str = "1y") -> pd.DataFrame:
        raise NotImplementedError
