from pathlib import Path
from pydantic import BaseModel, Field


class Settings(BaseModel):
    timezone: str = "Europe/Istanbul"
    universe_source: str = "csv"
    universe_path: str = "src/bot/universe/sample/bist100_sample.csv"
    use_is_suffix: bool = True
    min_price: float = 5.0
    min_liquidity_try: float = 20_000_000.0
    lookback_bars: int = 120
    risk_penalty_max: float = 40.0
    delta_threshold: float = 8.0
    cooldown_hours: int = 6

    account_size_try: float = 100_000.0
    risk_per_trade_pct: float = 1.0
    atr_stop_mult: float = 2.0
    trail_mult: float = 2.5
    tp1_r: float = 1.0
    tp2_r: float = 2.0
    max_hold_days: int = 5
    max_position_value_pct: float = 1.0
    max_positions: int = 1

    fee_bps: float = 10.0
    slippage_bps: float = 5.0
    weekly_flat: bool = True
    bear_entry_min: float = 75.0

    db_path: Path = Field(default=Path("signal_state.db"))


SETTINGS = Settings()
