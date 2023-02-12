import sqlite3
from pathlib import Path


def save_as_csv(df):
    file_path = Path("similarweb.csv")
    df.to_csv(file_path)


def save_as_sqlite(df):
    file_path = Path("similarweb.db")
    connection = sqlite3.connect(file_path)
    df.to_sql(name="similarweb", if_exists="replace", con=connection)
