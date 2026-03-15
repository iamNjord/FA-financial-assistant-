from datetime import datetime
from .models import Fill, Position, PortfolioState
from .rules import trailing_stop


def apply_slippage(price: float, side: str, bps: float) -> float:
    factor = 1 + (bps / 10000.0) if side == "BUY" else 1 - (bps / 10000.0)
    return price * factor


def fee_amount(notional: float, fee_bps: float) -> float:
    return notional * (fee_bps / 10000.0)


def update_position_bar(state: PortfolioState, pos: Position, now: datetime, close: float, atr14: float, trail_mult: float):
    pos.highest_since_entry = max(pos.highest_since_entry or pos.entry_price, close)
    pos.trailing_stop_price = trailing_stop(pos.highest_since_entry, atr14, trail_mult)
    if close <= pos.stop_price:
        return "STOP"
    if close <= pos.trailing_stop_price:
        return "TRAIL"
    if pos.planned_exit_time and now >= pos.planned_exit_time:
        return "TIME"
    return None


def close_position(state: PortfolioState, pos: Position, now: datetime, price: float, reason: str, fee_bps: float, slippage_bps: float):
    sell_price = apply_slippage(price, "SELL", slippage_bps)
    notional = sell_price * pos.qty
    fee = fee_amount(notional, fee_bps)
    pnl = (sell_price - pos.entry_price) * pos.qty - fee
    state.cash_try += notional - fee
    state.closed_trades.append({"symbol": pos.symbol, "exit_time": now.isoformat(), "reason": reason, "pnl": pnl})
    state.open_positions = [p for p in state.open_positions if p is not pos]
    return Fill(pos.symbol, now, "SELL", pos.qty, sell_price, fee)
