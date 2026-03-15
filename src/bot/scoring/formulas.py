from bot.features.normalization import clamp


def entry_score(momentum: float, trend: float, volume: float, setup: float, rs_component: float) -> float:
    base = 0.25 * momentum + 0.25 * trend + 0.2 * volume + 0.3 * setup
    return clamp(0.7 * base + 0.3 * rs_component)


def risk_score(vol: float, gap: float, liq: float, dd: float, flags: float) -> float:
    return clamp(0.3 * vol + 0.2 * gap + 0.2 * liq + 0.2 * dd + 0.1 * flags)


def composite_score(entry: float, risk: float, risk_penalty_max: float = 40.0) -> float:
    return entry - (risk / 100.0) * risk_penalty_max
