-- Retail Sales & Profitability Analysis
-- 03: Monthly Sales Trend and Growth

WITH Monthly_Sales AS (
    SELECT
        strftime('%Y-%m', Order_Date) AS Month,
        SUM(Sales) AS Total_Sales,
        SUM(Profit) AS Total_Profit
    FROM retail_sales_clean
    GROUP BY strftime('%Y-%m', Order_Date)
)
SELECT
    Month,
    Total_Sales,
    Total_Profit,
    LAG(Total_Sales) OVER (ORDER BY Month) AS Previous_Month_Sales,
    ROUND(
        (Total_Sales - LAG(Total_Sales) OVER (ORDER BY Month)) * 100.0
        / NULLIF(LAG(Total_Sales) OVER (ORDER BY Month), 0),
        2
    ) AS Sales_Growth_Percent
FROM Monthly_Sales
ORDER BY Month;