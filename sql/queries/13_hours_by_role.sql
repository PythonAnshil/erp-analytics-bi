SELECT
    e.role,
    ROUND(SUM(t.hours_worked), 2) AS total_hours,
    COUNT(DISTINCT e.employee_id) AS employee_count,
    ROUND(SUM(t.hours_worked) / NULLIF(COUNT(DISTINCT e.employee_id), 0), 2) AS avg_hours_per_employee
FROM clean_timesheets t
JOIN employees e
    ON t.employee_id = e.employee_id
GROUP BY e.role
ORDER BY total_hours DESC;