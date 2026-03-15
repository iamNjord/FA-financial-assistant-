def smooth_score(current: float, prev: float | None) -> float:
    if prev is None:
        return current
    return 0.7 * current + 0.3 * prev


def hysteresis_pass(prev: float | None, current: float, threshold: float = 8.0) -> bool:
    if prev is None:
        return True
    return abs(current - prev) >= threshold
