import pandas as pd
import sqlite3
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent

csv_file = PROJECT / "data" / "processed" / "retail_sales_clean.csv"
db_folder = PROJECT / "data"
db_folder.mkdir(parents=True, exist_ok=True)
db_file = db_folder / "retail_sales.db"

df = pd.read_csv(csv_file)

with sqlite3.connect(db_file) as conn:
    df.to_sql("sales", conn, if_exists="replace", index=False)

    result = pd.read_sql_query(
        "SELECT COUNT(*) AS total_rows FROM sales",
        conn
    )

    print("Rows loaded into SQL:", result.iloc[0]["total_rows"])
    print("Database saved to:", db_file)
