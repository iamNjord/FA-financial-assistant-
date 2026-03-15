def walkforward_windows(total_bars: int, train: int = 252, test: int = 63):
    i = 0
    while i + train + test <= total_bars:
        yield (i, i + train, i + train, i + train + test)
        i += test
