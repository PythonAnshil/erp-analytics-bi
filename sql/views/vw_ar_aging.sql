CREATE OR REPLACE VIEW vw_ar_aging AS
WITH payment_totals AS (
    SELECT
        invoice_id,
        COALESCE(SUM(amount_paid), 0) AS total_paid
    FROM clean_payments
    GROUP BY invoice_id
)
SELECT
    i.invoice_id,
    i.project_id,
    i.invoice_date,
    i.due_date,
    i.amount,
    i.status,
    COALESCE(p.total_paid, 0) AS total_paid,
    i.amount - COALESCE(p.total_paid, 0) AS outstanding_amount,
    CURRENT_DATE - i.due_date AS days_past_due,
    CASE
        WHEN i.amount - COALESCE(p.total_paid, 0) <= 0 THEN 'Paid'
        WHEN CURRENT_DATE <= i.due_date THEN 'Current'
        WHEN CURRENT_DATE - i.due_date BETWEEN 1 AND 30 THEN '1-30 Days'
        WHEN CURRENT_DATE - i.due_date BETWEEN 31 AND 60 THEN '31-60 Days'
        WHEN CURRENT_DATE - i.due_date BETWEEN 61 AND 90 THEN '61-90 Days'
        ELSE '90+ Days'
    END AS aging_bucket
FROM clean_invoices i
LEFT JOIN payment_totals p
    ON i.invoice_id = p.invoice_id;