import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

DATA_PATH = "data/raw"

def load_table(csv_file, table_name):

    print(f"Loading {table_name}...")

    df = pd.read_csv(f"{DATA_PATH}/{csv_file}")

    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False,
        method="multi",
        chunksize=5000
    )

    print(f"{table_name} loaded: {len(df)} rows")


if __name__ == "__main__":

    load_table("customers.csv", "customers")
    load_table("employees.csv", "employees")
    load_table("projects.csv", "projects")
    load_table("invoices.csv", "invoices")
    load_table("payments.csv", "payments")
    load_table("timesheets.csv", "timesheets")

    print("DATABASE LOAD COMPLETE")