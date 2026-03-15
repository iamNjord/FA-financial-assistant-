def mean_reversion_signal(close: float, sma20: float, rsi: float) -> bool:
    return close < sma20 and rsi < 35
