EXPLAIN ANALYZE
SELECT
    project_id,
    invoice_date,
    amount,
    status
FROM clean_invoices
WHERE project_id = 100
ORDER BY invoice_date DESC;