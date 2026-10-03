import os

import numpy as np
import pandas as pd
from sqlalchemy import create_engine


def generate_data():
    db_user = os.getenv("DB_USER", "admin")
    db_password = os.getenv("DB_PASSWORD", "password")
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "5432")
    db_name = os.getenv("DB_NAME", "insightledger")

    # Use postgresql+psycopg2 explicitly for SQLAlchemy 2.0 compatibility
    conn_str = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    engine = create_engine(conn_str)

    print("Generating mock user data...")
    # Users
    users_df = pd.DataFrame(
        {"user_id": range(1, 10001), "signup_date": pd.date_range(start="2023-01-01", periods=10000, freq="h")}
    )
    users_df.to_sql("users", engine, if_exists="replace", index=False)

    print("Generating A/B experiment data...")
    # Experiments (A/B Test)
    np.random.seed(42)
    variants = np.random.choice(["control", "treatment"], size=10000, p=[0.5, 0.5])
    converted = []

    # Intended Effect: Treatment performs slightly better
    for v in variants:
        if v == "control":
            converted.append(np.random.binomial(1, 0.10))
        else:
            converted.append(np.random.binomial(1, 0.125))

    experiments_df = pd.DataFrame({"user_id": range(1, 10001), "variant": variants, "converted": converted})
    experiments_df.to_sql("experiments", engine, if_exists="replace", index=False)

    print("Generating mock orders data...")
    # Orders
    converted_users = experiments_df[experiments_df["converted"] == 1]["user_id"]
    orders_df = pd.DataFrame(
        {
            "order_id": range(1, len(converted_users) + 1),
            "user_id": converted_users,
            "order_date": pd.date_range(start="2023-01-02", periods=len(converted_users), freq="h"),
            "amount": np.random.uniform(10, 100, size=len(converted_users)),
            "status": "completed",
        }
    )
    orders_df.to_sql("orders", engine, if_exists="replace", index=False)
    print("Database seeded successfully.")


if __name__ == "__main__":
    generate_data()
