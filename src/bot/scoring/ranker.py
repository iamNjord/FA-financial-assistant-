import pandas as pd


def rank_candidates(df_scores: pd.DataFrame, topn: int = 10) -> pd.DataFrame:
    return df_scores.sort_values("smoothed_score", ascending=False).head(topn)
