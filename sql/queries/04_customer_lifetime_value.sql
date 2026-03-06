SELECT
    customer_id,
    customer_name,
    total_projects,
    total_invoices,
    ROUND(total_revenue, 2) AS lifetime_value
FROM vw_customer_revenue
ORDER BY lifetime_value DESC;