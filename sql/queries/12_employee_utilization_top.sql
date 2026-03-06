SELECT
    employee_id,
    first_name,
    last_name,
    role,
    total_hours,
    capacity_hours,
    utilization_pct
FROM vw_employee_utilization
ORDER BY utilization_pct DESC
LIMIT 20;