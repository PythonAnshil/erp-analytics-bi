SELECT
    employee_id,
    first_name,
    last_name,
    role,
    total_hours,
    RANK() OVER (PARTITION BY role ORDER BY total_hours DESC) AS role_productivity_rank
FROM vw_employee_utilization
ORDER BY role, role_productivity_rank;