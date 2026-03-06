CREATE OR REPLACE VIEW vw_project_profitability AS
WITH labor_costs AS (
    SELECT
        t.project_id,
        COALESCE(SUM(t.hours_worked * e.hourly_rate), 0) AS labor_cost
    FROM clean_timesheets t
    JOIN employees e
        ON t.employee_id = e.employee_id
    GROUP BY t.project_id
),
project_revenue AS (
    SELECT
        project_id,
        COALESCE(SUM(amount), 0) AS revenue
    FROM clean_invoices
    GROUP BY project_id
)
SELECT
    p.project_id,
    p.project_name,
    p.customer_id,
    p.start_date,
    p.end_date,
    p.budget,
    p.status,
    COALESCE(r.revenue, 0) AS revenue,
    COALESCE(l.labor_cost, 0) AS labor_cost,
    COALESCE(r.revenue, 0) - COALESCE(l.labor_cost, 0) AS profit,
    CASE
        WHEN COALESCE(r.revenue, 0) = 0 THEN 0
        ELSE ROUND(((COALESCE(r.revenue, 0) - COALESCE(l.labor_cost, 0)) / r.revenue) * 100, 2)
    END AS profit_margin_pct
FROM clean_projects p
LEFT JOIN project_revenue r
    ON p.project_id = r.project_id
LEFT JOIN labor_costs l
    ON p.project_id = l.project_id;