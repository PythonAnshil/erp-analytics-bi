CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    industry VARCHAR(100),
    city VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    role VARCHAR(100),
    hourly_rate NUMERIC(10,2),
    hire_date DATE
);

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(255),
    customer_id INT REFERENCES customers(customer_id),
    start_date DATE,
    end_date DATE,
    budget NUMERIC(12,2),
    status VARCHAR(50)
);

CREATE TABLE timesheets (
    timesheet_id SERIAL PRIMARY KEY,
    employee_id INT REFERENCES employees(employee_id),
    project_id INT REFERENCES projects(project_id),
    work_date DATE,
    hours_worked NUMERIC(5,2)
);

CREATE TABLE invoices (
    invoice_id SERIAL PRIMARY KEY,
    project_id INT REFERENCES projects(project_id),
    invoice_date DATE,
    due_date DATE,
    amount NUMERIC(12,2),
    status VARCHAR(50)
);

CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    invoice_id INT REFERENCES invoices(invoice_id),
    payment_date DATE,
    amount_paid NUMERIC(12,2)
);