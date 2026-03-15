from dataclasses import dataclass


@dataclass
class StrategySignal:
    symbol: str
    action: str
    score: float
    reason: str
