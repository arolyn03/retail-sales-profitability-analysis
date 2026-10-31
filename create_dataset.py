import pandas as pd
from pathlib import Path

# Find your main project folder automatically
PROJECT = Path(__file__).resolve().parent.parent
RAW_DATA = PROJECT / "data" / "raw"
RAW_DATA.mkdir(parents=True, exist_ok=True)

data = {
    "Order_ID": ["O1001", "O1002", "O1003", "O1004", "O1005",
                 "O1006", "O1007", "O1008", "O1009", "O1010"],
    "Order_Date": ["2026-01-05", "2026-01-08", "2026-01-12",
                   "2026-01-15", "2026-02-02", "2026-02-07",
                   "2026-02-10", "2026-02-14", "2026-03-01", "2026-03-05"],
    "Region": ["South", "North", "East", "West", "South",
               "North", "East", "West", "South", "North"],
    "Category": ["Technology", "Furniture", "Office Supplies", "Technology",
                 "Furniture", "Technology", "Office Supplies", "Furniture",
                 "Technology", "Office Supplies"],
    "Sales": [1200, 850, 120, 2400, 950, 1800, 250, 1100, 3200, 180],
    "Cost": [800, 600, 70, 1500, 700, 1100, 140, 750, 2000, 100],
    "Quantity": [2, 1, 4, 3, 2, 2, 5, 2, 4, 3]
}

df = pd.DataFrame(data)
df.to_csv(RAW_DATA / "retail_sales_raw.csv", index=False)

print("Dataset created successfully!")
print("Rows:", len(df))
print(df.head())
print("Saved to:", RAW_DATA / "retail_sales_raw.csv")
