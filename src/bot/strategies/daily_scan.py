from .base import StrategySignal


def make_daily_signal(symbol: str, score: float, eligible: bool) -> StrategySignal:
    action = "BUY" if eligible else "HOLD"
    return StrategySignal(symbol=symbol, action=action, score=score, reason="daily_scan")
