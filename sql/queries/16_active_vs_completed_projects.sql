SELECT
    status,
    COUNT(*) AS project_count,
    ROUND(AVG(budget), 2) AS avg_budget
FROM clean_projects
GROUP BY status
ORDER BY project_count DESC;