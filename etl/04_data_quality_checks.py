import os
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

REPORT_DIR = "reports"
LOG_DIR = os.path.join(REPORT_DIR, "logs")
REPORT_PATH = os.path.join(REPORT_DIR, "data_quality_report.md")
LOG_PATH = os.path.join(LOG_DIR, "etl_run.log")

os.makedirs(REPORT_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)


CHECKS = {
    "raw_customers_count": "SELECT COUNT(*) FROM customers;",
    "raw_employees_count": "SELECT COUNT(*) FROM employees;",
    "raw_projects_count": "SELECT COUNT(*) FROM projects;",
    "raw_invoices_count": "SELECT COUNT(*) FROM invoices;",
    "raw_payments_count": "SELECT COUNT(*) FROM payments;",
    "raw_timesheets_count": "SELECT COUNT(*) FROM timesheets;",

    "clean_customers_count": "SELECT COUNT(*) FROM clean_customers;",
    "clean_projects_count": "SELECT COUNT(*) FROM clean_projects;",
    "clean_invoices_count": "SELECT COUNT(*) FROM clean_invoices;",
    "clean_payments_count": "SELECT COUNT(*) FROM clean_payments;",
    "clean_timesheets_count": "SELECT COUNT(*) FROM clean_timesheets;",

    "duplicate_customer_ids": """
        SELECT COUNT(*)
        FROM (
            SELECT customer_id
            FROM customers
            GROUP BY customer_id
            HAVING COUNT(*) > 1
        ) t;
    """,
    "duplicate_project_ids": """
        SELECT COUNT(*)
        FROM (
            SELECT project_id
            FROM projects
            GROUP BY project_id
            HAVING COUNT(*) > 1
        ) t;
    """,
    "duplicate_invoice_ids": """
        SELECT COUNT(*)
        FROM (
            SELECT invoice_id
            FROM invoices
            GROUP BY invoice_id
            HAVING COUNT(*) > 1
        ) t;
    """,
    "duplicate_payment_ids": """
        SELECT COUNT(*)
        FROM (
            SELECT payment_id
            FROM payments
            GROUP BY payment_id
            HAVING COUNT(*) > 1
        ) t;
    """,
    "duplicate_timesheet_ids": """
        SELECT COUNT(*)
        FROM (
            SELECT timesheet_id
            FROM timesheets
            GROUP BY timesheet_id
            HAVING COUNT(*) > 1
        ) t;
    """,

    "orphan_projects_customer": """
        SELECT COUNT(*)
        FROM projects p
        LEFT JOIN customers c
            ON p.customer_id = c.customer_id
        WHERE c.customer_id IS NULL;
    """,
    "orphan_invoices_project": """
        SELECT COUNT(*)
        FROM invoices i
        LEFT JOIN projects p
            ON i.project_id = p.project_id
        WHERE p.project_id IS NULL;
    """,
    "orphan_payments_invoice": """
        SELECT COUNT(*)
        FROM payments p
        LEFT JOIN invoices i
            ON p.invoice_id = i.invoice_id
        WHERE i.invoice_id IS NULL;
    """,
    "orphan_timesheets_employee": """
        SELECT COUNT(*)
        FROM timesheets t
        LEFT JOIN employees e
            ON t.employee_id = e.employee_id
        WHERE e.employee_id IS NULL;
    """,
    "orphan_timesheets_project": """
        SELECT COUNT(*)
        FROM timesheets t
        LEFT JOIN projects p
            ON t.project_id = p.project_id
        WHERE p.project_id IS NULL;
    """,

    "invalid_timesheet_hours_raw": """
        SELECT COUNT(*)
        FROM timesheets
        WHERE hours_worked < 0.5 OR hours_worked > 16;
    """,
    "invalid_timesheet_hours_clean": """
        SELECT COUNT(*)
        FROM clean_timesheets
        WHERE hours_worked < 0.5 OR hours_worked > 16;
    """,

    "total_invoice_amount": "SELECT COALESCE(SUM(amount), 0) FROM clean_invoices;",
    "total_payment_amount": "SELECT COALESCE(SUM(amount_paid), 0) FROM clean_payments;",
    "overdue_invoices_count": """
        SELECT COUNT(*)
        FROM clean_invoices
        WHERE due_date < CURRENT_DATE
          AND status IN ('pending', 'overdue');
    """
}


def run_scalar(query: str):
    with engine.connect() as conn:
        return conn.execute(text(query)).scalar()


def write_log(message: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


def main():
    results = {}

    with open(LOG_PATH, "w", encoding="utf-8") as f:
        f.write("ETL DATA QUALITY LOG\n")

    write_log("Starting data quality checks")

    for check_name, query in CHECKS.items():
        value = run_scalar(query)
        results[check_name] = value
        write_log(f"{check_name} = {value}")

    invoice_total = float(results["total_invoice_amount"] or 0)
    payment_total = float(results["total_payment_amount"] or 0)
    payment_coverage_ratio = 0 if invoice_total == 0 else round(payment_total / invoice_total, 4)

    report = f"""# Data Quality Report

Generated at: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## 1. Row Count Summary

| Check | Value |
|---|---:|
| Raw Customers | {results['raw_customers_count']} |
| Raw Employees | {results['raw_employees_count']} |
| Raw Projects | {results['raw_projects_count']} |
| Raw Invoices | {results['raw_invoices_count']} |
| Raw Payments | {results['raw_payments_count']} |
| Raw Timesheets | {results['raw_timesheets_count']} |
| Clean Customers | {results['clean_customers_count']} |
| Clean Projects | {results['clean_projects_count']} |
| Clean Invoices | {results['clean_invoices_count']} |
| Clean Payments | {results['clean_payments_count']} |
| Clean Timesheets | {results['clean_timesheets_count']} |

## 2. Primary Key Uniqueness Checks

| Check | Value |
|---|---:|
| Duplicate Customer IDs | {results['duplicate_customer_ids']} |
| Duplicate Project IDs | {results['duplicate_project_ids']} |
| Duplicate Invoice IDs | {results['duplicate_invoice_ids']} |
| Duplicate Payment IDs | {results['duplicate_payment_ids']} |
| Duplicate Timesheet IDs | {results['duplicate_timesheet_ids']} |

## 3. Referential Integrity Checks

| Check | Value |
|---|---:|
| Orphan Projects → Customers | {results['orphan_projects_customer']} |
| Orphan Invoices → Projects | {results['orphan_invoices_project']} |
| Orphan Payments → Invoices | {results['orphan_payments_invoice']} |
| Orphan Timesheets → Employees | {results['orphan_timesheets_employee']} |
| Orphan Timesheets → Projects | {results['orphan_timesheets_project']} |

## 4. Business Rule Checks

| Check | Value |
|---|---:|
| Invalid Timesheet Hours (Raw) | {results['invalid_timesheet_hours_raw']} |
| Invalid Timesheet Hours (Clean) | {results['invalid_timesheet_hours_clean']} |
| Overdue Invoices (Clean) | {results['overdue_invoices_count']} |

## 5. Financial Summary

| Check | Value |
|---|---:|
| Total Clean Invoice Amount | {invoice_total:.2f} |
| Total Clean Payment Amount | {payment_total:.2f} |
| Payment Coverage Ratio | {payment_coverage_ratio:.4f} |

## 6. Notes

- Clean-layer row counts may be lower than raw counts due to filtering and relational validation.
- Duplicate and orphan counts should ideally be zero.
- Invalid clean timesheet hours should be zero after cleaning.
- Payment coverage ratio below 1.0 is acceptable because not all invoices are expected to be paid.
"""

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report)

    write_log("Data quality report generated successfully")
    print("DATA QUALITY CHECKS COMPLETE")
    print(f"Report written to: {REPORT_PATH}")
    print(f"Log written to: {LOG_PATH}")


if __name__ == "__main__":
    main()