from .base import StrategySignal


def monday_entry(symbol: str, score: float, weekday: int) -> StrategySignal:
    ok = weekday == 0 and score >= 60
    return StrategySignal(symbol, "BUY" if ok else "HOLD", score, "monday_entry")
