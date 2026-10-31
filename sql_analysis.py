import sqlite3
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
db_file = PROJECT / "data" / "retail_sales.db"

query = """
SELECT
    Category,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    ROUND(100.0 * SUM(Profit) / SUM(Sales), 2) AS Profit_Margin_Pct
FROM sales
GROUP BY Category
ORDER BY Total_Profit DESC;
"""

with sqlite3.connect(db_file) as conn:
    cursor = conn.execute(query)

    print("Category Performance")
    print("-" * 75)

    for row in cursor.fetchall():
        print(row)
