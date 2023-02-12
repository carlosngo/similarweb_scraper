import pandas as pd
import globals


def plot_visits(df):
    visits_df = df[["domain", "visits_growth", "visits", "month"]]
    visits_df = visits_df.explode(["visits_growth", "visits", "month"])
    visits_df = visits_df.drop(visits_df[visits_df["visits"] == 0].index)
    visits_df["month"] = pd.Categorical(visits_df["month"], categories=globals.MONTHS, ordered=True)

    plot_visits_count(visits_df)
    plot_visits_growth(visits_df)


def plot_visits_count(df):
    visits_count_df = df[["domain", "visits", "month"]]
    visits_count_plot = visits_count_df \
        .pivot_table(values="visits", index="month", columns="domain") \
        .plot(logy=True, title="Month-on-month count on web visits", xlabel="Month", ylabel="Count on web visits")
    visits_count_figure = visits_count_plot.get_figure()
    visits_count_figure.savefig("visits_count.png")


def plot_visits_growth(df):
    visits_growth_df = df[["domain", "visits_growth", "month"]]
    visits_growth_df["visits_growth"] = visits_growth_df["visits_growth"] * 100
    visits_growth_plot = visits_growth_df \
        .pivot_table(values="visits_growth", index="month", columns="domain") \
        .plot(title="Month-on-month growth on web visits", xlabel="Month", ylabel="Growth on web visits (in %)")
    visits_growth_figure = visits_growth_plot.get_figure()
    visits_growth_figure.savefig("visits_growth.png")
