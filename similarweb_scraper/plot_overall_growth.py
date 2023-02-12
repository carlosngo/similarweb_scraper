def plot_overall_growth(df):
    growth_df = df[["domain", "avg_visits_growth", "avg_rank_growth"]]
    growth_df["overall_growth"] = (growth_df["avg_visits_growth"] * .5 + growth_df["avg_rank_growth"] * .5) * 100
    growth_df["rank"] = growth_df["overall_growth"].rank(method='dense', ascending=False).astype(int)
    growth_df["domain"] = growth_df["domain"].apply(lambda domain: domain[:-4])

    growth_df = growth_df[["domain", "overall_growth"]].sort_values("overall_growth", ascending=False)

    growth_plot = growth_df.plot.bar(x="domain", y="overall_growth", title="Overall growth by domain, ranked",
                                     xlabel="Domain", ylabel="Overall Growth (in %)", rot=0, legend=False)
    growth_figure = growth_plot.get_figure()
    growth_figure.savefig("overall_growth.png")
