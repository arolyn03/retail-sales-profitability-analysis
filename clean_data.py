import pandas as pd
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent

raw_file = PROJECT / "data" / "raw" / "retail_sales_raw.csv"
processed_folder = PROJECT / "data" / "processed"
processed_folder.mkdir(parents=True, exist_ok=True)

# 1. Load the raw dat   a
df = pd.read_csv(raw_file)

print("Original rows:", len(df))
print("Missing values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

# 2. Convert the date column
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

# 3. Remove duplicate records
df = df.drop_duplicates()

# 4. Validate essential fields
df = df.dropna(subset=["Order_ID", "Order_Date", "Sales", "Cost"])
df = df[(df["Sales"] >= 0) & (df["Cost"] >= 0)]

# 5. Create new business metrics
df["Profit"] = df["Sales"] - df["Cost"]
df["Profit_Margin"] = (
    df["Profit"] / df["Sales"].where(df["Sales"] != 0)
)

# 6. Add useful date fields
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

# 7. Export the cleaned data
output_file = processed_folder / "retail_sales_clean.csv"
df.to_csv(output_file, index=False)

print("\nCleaned rows:", len(df))
print("Total sales:", df["Sales"].sum())
print("Total profit:", df["Profit"].sum())
print("Saved to:", output_file)
print("\nPreview:")
print(df.head())
