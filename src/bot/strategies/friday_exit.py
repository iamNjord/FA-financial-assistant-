from .base import StrategySignal


def friday_exit(symbol: str, risk_score: float, weekday: int, weekly_flat: bool = True) -> StrategySignal:
    exit_now = weekday == 4 and (weekly_flat or risk_score > 60)
    return StrategySignal(symbol, "SELL" if exit_now else "HOLD", 100 - risk_score, "friday_exit")
