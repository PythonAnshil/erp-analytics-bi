SELECT
    customer_id,
    customer_name,
    total_projects,
    total_revenue,
    NTILE(4) OVER (ORDER BY total_revenue DESC) AS revenue_quartile
FROM vw_customer_revenue
ORDER BY total_revenue DESC;