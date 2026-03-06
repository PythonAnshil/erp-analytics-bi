WITH invoice_totals AS (
    SELECT
        project_id,
        SUM(amount) AS total_invoiced
    FROM clean_invoices
    GROUP BY project_id
),
payment_totals AS (
    SELECT
        i.project_id,
        SUM(p.amount_paid) AS total_paid
    FROM clean_invoices i
    LEFT JOIN clean_payments p
        ON i.invoice_id = p.invoice_id
    GROUP BY i.project_id
)
SELECT
    i.project_id,
    ROUND(i.total_invoiced, 2) AS total_invoiced,
    ROUND(COALESCE(p.total_paid, 0), 2) AS total_paid,
    ROUND(
        CASE
            WHEN i.total_invoiced = 0 THEN 0
            ELSE COALESCE(p.total_paid, 0) / i.total_invoiced * 100
        END, 2
    ) AS payment_coverage_pct
FROM invoice_totals i
LEFT JOIN payment_totals p
    ON i.project_id = p.project_id
ORDER BY payment_coverage_pct ASC;