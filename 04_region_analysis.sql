-- Retail Sales & Profitability Analysis
-- 04: Region-wise Sales and Profitability

SELECT
    Region,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    ROUND(
        SUM(Profit) * 100.0 / NULLIF(SUM(Sales), 0),
        2
    ) AS Profit_Margin_Percent
FROM retail_sales_clean
GROUP BY Region
ORDER BY Total_Sales DESC;