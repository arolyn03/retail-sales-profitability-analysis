import sqlite3
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
db_file = PROJECT / "data" / "retail_sales.db"

query = """
WITH monthly_sales AS (
    SELECT
        Month,
        SUM(Sales) AS Total_Sales,
        SUM(Profit) AS Total_Profit
    FROM sales
    GROUP BY Month
)
SELECT
    Month,
    Total_Sales,
    Total_Profit,
    LAG(Total_Sales) OVER (ORDER BY Month) AS Previous_Month_Sales,
    ROUND(
        100.0 * (
            Total_Sales - LAG(Total_Sales) OVER (ORDER BY Month)
        ) / NULLIF(LAG(Total_Sales) OVER (ORDER BY Month), 0),
        2
    ) AS Sales_Growth_Pct
FROM monthly_sales
ORDER BY Month;
"""

with sqlite3.connect(db_file) as conn:
    for row in conn.execute(query):
        print(row)
