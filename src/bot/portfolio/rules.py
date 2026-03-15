def initial_stop(entry_price: float, atr14: float, atr_mult: float) -> float:
    return entry_price - atr14 * atr_mult


def trailing_stop(highest_since_entry: float, atr14: float, trail_mult: float) -> float:
    return highest_since_entry - atr14 * trail_mult


def tp_price(entry_price: float, initial_stop_price: float, r_mult: float) -> float:
    r = entry_price - initial_stop_price
    return entry_price + r_mult * r
