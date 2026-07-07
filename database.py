import sqlite3
import pandas as pd


def create_database():
    df = pd.read_csv("data/employee_attrition.csv")
    conn = sqlite3.connect("hr_analytics.db")

    df.to_sql(
        "employee_attrition",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()
    print("✅ Database created successfully!")

if __name__ == "__main__":
    create_database()