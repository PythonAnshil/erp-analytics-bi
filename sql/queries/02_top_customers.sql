SELECT
    customer_id,
    customer_name,
    total_revenue,
    RANK() OVER (ORDER BY total_revenue DESC) AS revenue_rank
FROM vw_customer_revenue
ORDER BY total_revenue DESC
LIMIT 10;