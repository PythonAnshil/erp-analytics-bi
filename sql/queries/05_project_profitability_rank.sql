SELECT
    project_id,
    project_name,
    revenue,
    labor_cost,
    profit,
    profit_margin_pct,
    DENSE_RANK() OVER (ORDER BY profit DESC) AS profit_rank
FROM vw_project_profitability
ORDER BY profit DESC
LIMIT 15;