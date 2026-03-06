SELECT
    DATE_TRUNC('month', work_date)::date AS work_month,
    project_id,
    ROUND(SUM(hours_worked), 2) AS total_hours
FROM clean_timesheets
GROUP BY 1, 2
ORDER BY work_month, total_hours DESC;