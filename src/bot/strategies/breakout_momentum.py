def breakout_signal(close: float, high20: float) -> bool:
    return close > high20
