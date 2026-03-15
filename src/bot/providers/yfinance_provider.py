import yfinance as yf
from tenacity import retry, stop_after_attempt, wait_fixed
from .base import DataProvider


class YFinanceProvider(DataProvider):
    @retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
    def fetch_ohlcv(self, symbol: str, interval: str = "1d", lookback: str = "1y"):
        df = yf.download(symbol, period=lookback, interval=interval, auto_adjust=False, progress=False)
        if df.empty:
            return df
        df.columns = [c.lower() for c in df.columns]
        return df.rename(columns={"adj close": "adj_close"})
