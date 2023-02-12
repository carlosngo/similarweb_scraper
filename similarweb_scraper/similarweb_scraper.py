from data_collection import collect_data
from data_storage import save_as_csv, save_as_sqlite
from data_processing import process_data
from plot_visits import plot_visits
from plot_rank import plot_rank
from plot_overall_growth import plot_overall_growth


def main():
    df = collect_data()
    save_as_csv(df)
    save_as_sqlite(df)

    df = process_data(df)
    plot_visits(df)
    plot_rank(df)
    plot_overall_growth(df)


if __name__ == "__main__":
    main()
