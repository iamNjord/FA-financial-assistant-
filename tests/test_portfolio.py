from datetime import datetime, timedelta
from bot.portfolio.sizing import risk_based_qty
from bot.portfolio.rules import initial_stop, tp_price
from bot.portfolio.models import PortfolioState, Position
from bot.portfolio.simulator import apply_slippage, fee_amount, update_position_bar


def test_risk_based_sizing():
    qty, flag = risk_based_qty(100000, 1.0, atr14=2, atr_mult=2, price=100, cash=100000)
    assert qty > 0 and flag is None


def test_stops_tp_time_stop_and_costs():
    stop = initial_stop(100, 2, 2)
    assert stop == 96
    assert tp_price(100, stop, 1.0) == 104
    assert round(apply_slippage(100, "BUY", 5), 2) == 100.05
    assert fee_amount(10000, 10) == 10
    state = PortfolioState(cash_try=100000, equity=100000)
    pos = Position(symbol="THYAO.IS", entry_time=datetime.now(), entry_price=100, qty=10, stop_price=95, planned_exit_time=datetime.now()+timedelta(days=1))
    reason = update_position_bar(state, pos, datetime.now()+timedelta(days=2), close=100, atr14=2, trail_mult=2.5)
    assert reason == "TIME"
