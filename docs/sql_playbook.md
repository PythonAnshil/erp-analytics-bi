# SQL Playbook

## Overview
This document explains the purpose of each SQL query in the ERP Analytics & BI project.

## Query List

### 01_revenue_by_month.sql
Shows monthly revenue trend using aggregation and date truncation.

### 02_top_customers.sql
Ranks highest revenue customers using a window ranking function.

### 03_revenue_by_industry.sql
Aggregates revenue by customer industry.

### 04_customer_lifetime_value.sql
Measures total customer value across invoices and projects.

### 05_project_profitability_rank.sql
Ranks projects by profit using the profitability warehouse view.

### 06_projects_over_budget_risk.sql
Flags projects by budget risk using CASE logic.

### 07_revenue_per_project.sql
Calculates total invoiced revenue at project level with joins.

### 08_monthly_running_revenue.sql
Computes running total revenue over time using a window function.

### 09_overdue_invoices.sql
Lists outstanding overdue invoices for receivables analysis.

### 10_ar_aging_summary.sql
Summarizes receivables by aging bucket.

### 11_payment_coverage_by_project.sql
Compares invoiced vs paid value by project.

### 12_employee_utilization_top.sql
Shows top employees by utilization percentage.

### 13_hours_by_role.sql
Analyzes workload by employee role.

### 14_employee_productivity_rank.sql
Ranks employees within role by hours worked.

### 15_project_hours_by_month.sql
Tracks project labor trends by month.

### 16_active_vs_completed_projects.sql
Compares project volumes and budgets by status.

### 17_invoice_status_distribution.sql
Analyzes invoice counts and amounts by status.

### 18_customer_project_concentration.sql
Segments customers into revenue quartiles using NTILE.

### 19_month_over_month_revenue_change.sql
Measures month-over-month revenue change using LAG.

### 20_explain_plan_invoice_lookup.sql
Demonstrates query performance analysis with EXPLAIN ANALYZE.

## SQL Features Covered
- Joins
- CTEs
- Window functions
- Aggregations
- CASE expressions
- Date calculations
- Ranking
- Running totals
- Query performance analysis