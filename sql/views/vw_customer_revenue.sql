CREATE OR REPLACE VIEW vw_customer_revenue AS
SELECT
    c.customer_id,
    c.customer_name,
    c.industry,
    c.city,
    COUNT(DISTINCT p.project_id) AS total_projects,
    COUNT(DISTINCT i.invoice_id) AS total_invoices,
    COALESCE(SUM(i.amount), 0) AS total_revenue,
    COALESCE(SUM(py.amount_paid), 0) AS total_payments_received
FROM clean_customers c
LEFT JOIN clean_projects p
    ON c.customer_id = p.customer_id
LEFT JOIN clean_invoices i
    ON p.project_id = i.project_id
LEFT JOIN clean_payments py
    ON i.invoice_id = py.invoice_id
GROUP BY
    c.customer_id,
    c.customer_name,
    c.industry,
    c.city;