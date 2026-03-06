SELECT
    COALESCE(industry, 'Unknown') AS industry,
    ROUND(SUM(total_revenue), 2) AS revenue
FROM vw_customer_revenue
GROUP BY 1
ORDER BY revenue DESC;