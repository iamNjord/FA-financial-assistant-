from bot.universe.loader import load_universe


def test_load_csv_and_json():
    csv_syms = load_universe("csv", "src/bot/universe/sample/bist100_sample.csv", True)
    json_syms = load_universe("json", "src/bot/universe/sample/bist100_sample.json", True)
    assert csv_syms[0] == "THYAO.IS"
    assert json_syms[1] == "ASELS.IS"
