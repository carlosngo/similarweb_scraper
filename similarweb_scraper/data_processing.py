import globals


def process_data(df):
    df_p = df

    df_p["month"] = [globals.MONTHS] * len(df_p)

    df_p[["dec_visits_growth", "nov_visits_growth", "oct_visits_growth"]] \
        = df_p[["dec_visits", "nov_visits", "oct_visits"]].pct_change(axis="columns", periods=-1)
    df_p["avg_visits_growth"] = (df_p["dec_visits_growth"] + df_p["nov_visits_growth"]) / 2

    df_p[["dec_rank_growth", "nov_rank_growth", "oct_rank_growth"]] \
        = df_p[["dec_rank", "nov_rank", "oct_rank"]].pct_change(axis="columns", periods=-1)
    df_p["avg_rank_growth"] = (df_p["dec_rank_growth"] + df_p["nov_rank_growth"]) / 2

    df_p = df_p.fillna(0)

    df_p["visits"] = df_p[["oct_visits", "nov_visits", "dec_visits"]].apply(tuple, axis=1)
    df_p["visits_growth"] = df_p[["oct_visits_growth", "nov_visits_growth", "dec_visits_growth"]].apply(tuple, axis=1)

    df_p["rank"] = df_p[["oct_rank", "nov_rank", "dec_rank"]].apply(tuple, axis=1)
    df_p["rank_growth"] = df_p[["oct_rank_growth", "nov_rank_growth", "dec_rank_growth"]].apply(tuple, axis=1)

    return df_p
