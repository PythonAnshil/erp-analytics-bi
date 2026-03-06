SELECT
    aging_bucket,
    COUNT(*) AS invoice_count,
    ROUND(SUM(outstanding_amount), 2) AS total_outstanding
FROM vw_ar_aging
GROUP BY aging_bucket
ORDER BY total_outstanding DESC;