SELECT
    DATE_TRUNC('month', invoice_date)::date AS revenue_month,
    ROUND(SUM(amount), 2) AS monthly_revenue
FROM clean_invoices
GROUP BY 1
ORDER BY 1;