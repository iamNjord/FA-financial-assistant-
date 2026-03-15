def passes_filters(price: float, liquidity_try: float, lookback: int, min_price: float = 5.0, min_liq: float = 20_000_000) -> bool:
    return price >= min_price and liquidity_try >= min_liq and lookback >= 120
