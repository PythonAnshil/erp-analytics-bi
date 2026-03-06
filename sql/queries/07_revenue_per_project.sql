SELECT
    p.project_id,
    p.project_name,
    c.customer_name,
    ROUND(COALESCE(SUM(i.amount), 0), 2) AS project_revenue
FROM clean_projects p
JOIN clean_customers c
    ON p.customer_id = c.customer_id
LEFT JOIN clean_invoices i
    ON p.project_id = i.project_id
GROUP BY
    p.project_id,
    p.project_name,
    c.customer_name
ORDER BY project_revenue DESC;