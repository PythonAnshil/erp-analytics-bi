SELECT
    status,
    COUNT(*) AS invoice_count,
    ROUND(SUM(amount), 2) AS total_amount
FROM clean_invoices
GROUP BY status
ORDER BY total_amount DESC;