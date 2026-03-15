import math


def risk_based_qty(account_size: float, risk_per_trade_pct: float, atr14: float, atr_mult: float, price: float, cash: float, max_position_value_pct: float = 1.0) -> tuple[int, str | None]:
    stop_distance = atr14 * atr_mult
    if stop_distance <= 0:
        return 0, "INVALID_STOP_DISTANCE"
    risk_try = account_size * (risk_per_trade_pct / 100.0)
    qty = math.floor(risk_try / stop_distance)
    max_by_cash = math.floor((cash * max_position_value_pct) / price)
    qty = min(qty, max_by_cash)
    if qty < 1:
        return 0, "NOT_TRADEABLE_BY_RISK"
    return qty, None
