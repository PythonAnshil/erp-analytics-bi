CREATE OR REPLACE VIEW vw_employee_utilization AS
WITH employee_hours AS (
    SELECT
        e.employee_id,
        e.first_name,
        e.last_name,
        e.role,
        COUNT(DISTINCT t.work_date) AS days_worked,
        COALESCE(SUM(t.hours_worked), 0) AS total_hours
    FROM employees e
    LEFT JOIN clean_timesheets t
        ON e.employee_id = t.employee_id
    GROUP BY
        e.employee_id,
        e.first_name,
        e.last_name,
        e.role
)
SELECT
    employee_id,
    first_name,
    last_name,
    role,
    days_worked,
    total_hours,
    ROUND(days_worked * 8.0, 2) AS capacity_hours,
    CASE
        WHEN days_worked = 0 THEN 0
        ELSE ROUND((total_hours / (days_worked * 8.0)) * 100, 2)
    END AS utilization_pct
FROM employee_hours;