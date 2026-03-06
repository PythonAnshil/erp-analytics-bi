SELECT
    project_id,
    project_name,
    budget,
    labor_cost,
    revenue,
    profit,
    CASE
        WHEN labor_cost > budget THEN 'Over Budget'
        WHEN labor_cost >= budget * 0.9 THEN 'Near Budget Limit'
        ELSE 'Within Budget'
    END AS budget_risk_flag
FROM vw_project_profitability
ORDER BY labor_cost DESC;