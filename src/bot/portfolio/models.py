from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Fill:
    symbol: str
    time: datetime
    side: str
    qty: int
    price: float
    fee: float


@dataclass
class OrderSim:
    symbol: str
    side: str
    qty: int
    ref_price: float


@dataclass
class Position:
    symbol: str
    entry_time: datetime
    entry_price: float
    qty: int
    stop_price: float
    take_profit_price: float | None = None
    trailing_stop_price: float | None = None
    partial_taken: bool = False
    highest_since_entry: float | None = None
    planned_exit_time: datetime | None = None
    strategy_tag: str = ""
    entry_reason: str = ""


@dataclass
class PortfolioState:
    cash_try: float
    equity: float
    open_positions: list[Position] = field(default_factory=list)
    closed_trades: list[dict] = field(default_factory=list)
    max_positions: int = 1
    max_exposure_pct: float = 1.0
