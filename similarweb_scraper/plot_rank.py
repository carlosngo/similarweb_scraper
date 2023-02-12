import pandas as pd
import globals


def plot_rank(df):
    rank_df = df[["domain", "rank_growth", "rank", "month"]]
    rank_df = rank_df.explode(["rank_growth", "rank", "month"])
    rank_df["month"] = pd.Categorical(rank_df["month"], categories=globals.MONTHS, ordered=True)

    plot_rank_count(rank_df)
    plot_rank_growth(rank_df)


def plot_rank_count(df):
    rank_count_df = df[["domain", "rank", "month"]]
    rank_count_plot = rank_count_df \
        .pivot_table(values="rank", index="month", columns="domain") \
        .plot(logy=True, title="Month-on-month count on web rank", xlabel="Month", ylabel="Count on web rank")
    rank_count_figure = rank_count_plot.get_figure()
    rank_count_figure.savefig("rank_count.png")


def plot_rank_growth(df):
    rank_growth_df = df[["domain", "rank_growth", "month"]]
    rank_growth_df["rank_growth"] = rank_growth_df["rank_growth"] * 100
    rank_growth_plot = rank_growth_df \
        .pivot_table(values="rank_growth", index="month", columns="domain") \
        .plot(title="Month-on-month growth on web rank", xlabel="Month", ylabel="Growth on web rank (in %)")
    rank_growth_figure = rank_growth_plot.get_figure()
    rank_growth_figure.savefig("rank_growth.png")
