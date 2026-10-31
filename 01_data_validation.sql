-- Retail Sales & Profitability Analysis
-- 01: Data Validation

SELECT
    COUNT(*) AS total_orders,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM retail_sales_clean;