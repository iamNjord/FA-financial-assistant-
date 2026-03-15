from bot.portfolio.models import PortfolioState


def run_portfolio_backtest(initial_cash: float = 100000.0) -> PortfolioState:
    return PortfolioState(cash_try=initial_cash, equity=initial_cash)
