WITH monthly_revenue AS (
    SELECT
        DATE_TRUNC('month', invoice_date)::date AS revenue_month,
        SUM(amount) AS monthly_revenue
    FROM clean_invoices
    GROUP BY 1
)
SELECT
    revenue_month,
    ROUND(monthly_revenue, 2) AS monthly_revenue,
    ROUND(
        LAG(monthly_revenue) OVER (ORDER BY revenue_month),
        2
    ) AS previous_month_revenue,
    ROUND(
        monthly_revenue - COALESCE(LAG(monthly_revenue) OVER (ORDER BY revenue_month), 0),
        2
    ) AS revenue_change
FROM monthly_revenue
ORDER BY revenue_month;