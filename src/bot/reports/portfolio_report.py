from bot.portfolio.models import PortfolioState


def snapshot(state: PortfolioState) -> dict:
    open_pos = state.open_positions[0] if state.open_positions else None
    return {
        "cash": state.cash_try,
        "equity": state.equity,
        "open_symbol": open_pos.symbol if open_pos else None,
        "open_qty": open_pos.qty if open_pos else 0,
    }
