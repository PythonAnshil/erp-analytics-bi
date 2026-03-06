import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta
import os

fake = Faker()

OUTPUT_DIR = "data/raw"
os.makedirs(OUTPUT_DIR, exist_ok=True)

NUM_CUSTOMERS = 500
NUM_EMPLOYEES = 250
NUM_PROJECTS = 2000
NUM_INVOICES = 20000
NUM_PAYMENTS = 15000
NUM_TIMESHEETS = 150000


def generate_customers():
    data = []

    industries = ["Finance", "Healthcare", "Technology", "Retail", "Manufacturing", None]

    for i in range(NUM_CUSTOMERS):
        data.append({
            "customer_name": fake.company(),
            "industry": random.choice(industries),
            "city": fake.city()
        })

    df = pd.DataFrame(data)
    df.to_csv(f"{OUTPUT_DIR}/customers.csv", index=False)
    print("customers generated")


def generate_employees():
    roles = ["Developer", "Consultant", "Manager", "Analyst", "Support"]

    data = []

    for i in range(NUM_EMPLOYEES):
        data.append({
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "role": random.choice(roles),
            "hourly_rate": round(random.uniform(40,120),2),
            "hire_date": fake.date_between(start_date="-5y", end_date="today")
        })

    df = pd.DataFrame(data)
    df.to_csv(f"{OUTPUT_DIR}/employees.csv", index=False)
    print("employees generated")


def generate_projects():
    statuses = ["active","completed","on_hold"]

    data = []

    for i in range(NUM_PROJECTS):
        start = fake.date_between(start_date="-3y", end_date="-30d")
        end = start + timedelta(days=random.randint(30,365))

        data.append({
            "project_name": fake.bs(),
            "customer_id": random.randint(1,NUM_CUSTOMERS),
            "start_date": start,
            "end_date": end,
            "budget": round(random.uniform(20000,500000),2),
            "status": random.choice(statuses)
        })

    df = pd.DataFrame(data)
    df.to_csv(f"{OUTPUT_DIR}/projects.csv", index=False)
    print("projects generated")


def generate_invoices():
    statuses = ["paid","pending","overdue"]

    data = []

    for i in range(NUM_INVOICES):

        invoice_date = fake.date_between(start_date="-2y", end_date="today")
        due_date = invoice_date + timedelta(days=30)

        data.append({
            "project_id": random.randint(1,NUM_PROJECTS),
            "invoice_date": invoice_date,
            "due_date": due_date,
            "amount": round(random.uniform(2000,50000),2),
            "status": random.choice(statuses)
        })

    df = pd.DataFrame(data)
    df.to_csv(f"{OUTPUT_DIR}/invoices.csv", index=False)
    print("invoices generated")


def generate_payments():

    data = []

    for i in range(NUM_PAYMENTS):

        payment_date = fake.date_between(start_date="-2y", end_date="today")

        data.append({
            "invoice_id": random.randint(1,NUM_INVOICES),
            "payment_date": payment_date,
            "amount_paid": round(random.uniform(2000,50000),2)
        })

    df = pd.DataFrame(data)
    df.to_csv(f"{OUTPUT_DIR}/payments.csv", index=False)
    print("payments generated")


def generate_timesheets():

    data = []

    for i in range(NUM_TIMESHEETS):

        data.append({
            "employee_id": random.randint(1,NUM_EMPLOYEES),
            "project_id": random.randint(1,NUM_PROJECTS),
            "work_date": fake.date_between(start_date="-1y", end_date="today"),
            "hours_worked": round(random.uniform(1,10),2)
        })

    df = pd.DataFrame(data)
    df.to_csv(f"{OUTPUT_DIR}/timesheets.csv", index=False)
    print("timesheets generated")


if __name__ == "__main__":

    generate_customers()
    generate_employees()
    generate_projects()
    generate_invoices()
    generate_payments()
    generate_timesheets()

    print("DATA GENERATION COMPLETE")