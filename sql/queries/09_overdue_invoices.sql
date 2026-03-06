SELECT
    invoice_id,
    project_id,
    due_date,
    outstanding_amount,
    days_past_due,
    aging_bucket
FROM vw_ar_aging
WHERE outstanding_amount > 0
  AND aging_bucket <> 'Current'
  AND aging_bucket <> 'Paid'
ORDER BY days_past_due DESC;