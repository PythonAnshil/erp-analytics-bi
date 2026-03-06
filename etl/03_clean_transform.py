import os
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

SQL_STATEMENTS = [
    """
    DROP TABLE IF EXISTS clean_customers;
    CREATE TABLE clean_customers AS
    SELECT
        customer_id,
        TRIM(customer_name) AS customer_name,
        INITCAP(TRIM(industry)) AS industry,
        INITCAP(TRIM(city)) AS city,
        created_at
    FROM customers;
    """,
    """
    DROP TABLE IF EXISTS clean_projects;
    CREATE TABLE clean_projects AS
    SELECT
        p.project_id,
        TRIM(p.project_name) AS project_name,
        p.customer_id,
        p.start_date,
        p.end_date,
        p.budget,
        LOWER(TRIM(p.status)) AS status
    FROM projects p
    INNER JOIN clean_customers c
        ON p.customer_id = c.customer_id;
    """,
    """
    DROP TABLE IF EXISTS clean_timesheets;
    CREATE TABLE clean_timesheets AS
    SELECT
        t.timesheet_id,
        t.employee_id,
        t.project_id,
        t.work_date,
        t.hours_worked
    FROM timesheets t
    INNER JOIN employees e
        ON t.employee_id = e.employee_id
    INNER JOIN clean_projects p
        ON t.project_id = p.project_id
    WHERE t.hours_worked BETWEEN 0.5 AND 16;
    """,
    """
    DROP TABLE IF EXISTS clean_invoices;
    CREATE TABLE clean_invoices AS
    SELECT
        i.invoice_id,
        i.project_id,
        i.invoice_date,
        i.due_date,
        i.amount,
        LOWER(TRIM(i.status)) AS status
    FROM invoices i
    INNER JOIN clean_projects p
        ON i.project_id = p.project_id
    WHERE i.amount > 0;
    """,
    """
    DROP TABLE IF EXISTS clean_payments;
    CREATE TABLE clean_payments AS
    SELECT
        p.payment_id,
        p.invoice_id,
        p.payment_date,
        p.amount_paid
    FROM payments p
    INNER JOIN clean_invoices i
        ON p.invoice_id = i.invoice_id
    WHERE p.amount_paid > 0;
    """
]


def run_cleaning_pipeline():
    with engine.begin() as conn:
        for idx, stmt in enumerate(SQL_STATEMENTS, start=1):
            print(f"Running cleaning step {idx}...")
            conn.execute(text(stmt))
    print("CLEANING PIPELINE COMPLETE")


if __name__ == "__main__":
    run_cleaning_pipeline()