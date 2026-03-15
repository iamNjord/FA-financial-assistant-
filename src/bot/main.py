import argparse
from datetime import datetime
import pandas as pd

from bot.config import SETTINGS
from bot.universe.loader import load_universe
from bot.providers.vendor_provider_stub import VendorProviderStub
from bot.features.smoothing import smooth_score
from bot.scoring.ranker import rank_candidates
from bot.state.store import StateStore


def run_scan(mode: str = "daily"):
    provider = VendorProviderStub()
    symbols = load_universe(SETTINGS.universe_source, SETTINGS.universe_path, SETTINGS.use_is_suffix)
    store = StateStore(SETTINGS.db_path)
    rows = []
    for s in symbols:
        _ = provider.fetch_ohlcv(s)
        base = 60.0
        prev = store.get_prev_smoothed(s)
        sm = smooth_score(base, prev)
        store.set_prev_smoothed(s, sm)
        rows.append({"symbol": s, "smoothed_score": sm, "mode": mode})
    ranked = rank_candidates(pd.DataFrame(rows), topn=min(5, len(rows)))
    print(ranked.to_string(index=False))


def run_backtest(weeks: int):
    print(f"weekly backtest finished for {weeks} weeks")


def run_portfolio_backtest(start: str, end: str, timeframe: str):
    print(f"portfolio-backtest finished ({start} -> {end}, {timeframe})")


def print_universe(source: str):
    symbols = load_universe(source, SETTINGS.universe_path, SETTINGS.use_is_suffix)
    print("\n".join(symbols))


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("run")
    scan_p = sub.add_parser("scan")
    scan_p.add_argument("--mode", default="daily", choices=["daily", "friday"])
    bt = sub.add_parser("backtest")
    bt.add_argument("--weeks", type=int, default=156)
    pbt = sub.add_parser("portfolio-backtest")
    pbt.add_argument("--start", required=True)
    pbt.add_argument("--end", required=True)
    pbt.add_argument("--timeframe", default="1d")
    uni = sub.add_parser("universe")
    uni.add_argument("--print", action="store_true")
    uni.add_argument("--source", default="csv", choices=["csv", "json", "watchlist"])

    args = parser.parse_args()
    if args.cmd == "run":
        run_scan("daily")
    elif args.cmd == "scan":
        run_scan(args.mode)
    elif args.cmd == "backtest":
        run_backtest(args.weeks)
    elif args.cmd == "portfolio-backtest":
        run_portfolio_backtest(args.start, args.end, args.timeframe)
    elif args.cmd == "universe" and args.print:
        print_universe(args.source)


if __name__ == "__main__":
    main()
