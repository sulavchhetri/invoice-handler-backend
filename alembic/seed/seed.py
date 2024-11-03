import os
from dotenv import load_dotenv
from src.utils.util import get_extra_keys
from src.crud import create_invoice, truncate_invoice_table
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

data = {
    "1": {
        "task": "Task 1",
        "hours": 40,
        "unit_price": 150,
        "discount": 20,
        "amount": 3000,
        "task_id": "1",
        "1.1": {
            "task": "Task 1.1",
            "hours": 60,
            "unit_price": 20,
            "discount": 10,
            "amount": 2000,
            "task_id": "1.1",
            "1.1.1": {
                "task": "Task 1.1.1",
                "hours": 30,
                "unit_price": 25,
                "discount": 5,
                "amount": 750,
                "task_id": "1.1.1",
            },
        },
        "1.2": {
            "task": "Task 1.2",
            "hours": 120,
            "unit_price": 30,
            "discount": 50,
            "amount": 1000,
            "task_id": "1.2",
        },
    },
    "2": {
        "task": "Task 2",
        "hours": 30,
        "unit_price": 300,
        "discount": 25,
        "amount": 500,
        "task_id": "2",
        "2.1": {
            "task": "Task 2.1",
            "hours": 45,
            "unit_price": 200,
            "discount": 15,
            "amount": 7200,
            "task_id": "2.1",
        },
    },
    "3": {
        "task": "Task 3",
        "hours": 100,
        "unit_price": 25,
        "discount": 15,
        "amount": 100,
        "task_id": "3",
        "3.1": {
            "task": "Task 3.1",
            "hours": 80,
            "unit_price": 100,
            "discount": 10,
            "amount": 8000,
            "task_id": "3.1",
            "3.1.1": {
                "task": "Task 3.1.1",
                "hours": 50,
                "unit_price": 50,
                "discount": 20,
                "amount": 2500,
                "task_id": "3.1.1",
            },
        },
    },
    "4": {
        "task": "Task 4",
        "hours": 8,
        "unit_price": 600,
        "discount": 1000,
        "amount": 1500,
        "task_id": "4",
    },
    "5": {
        "task": "Task 5",
        "hours": 100,
        "unit_price": 500,
        "discount": 2500,
        "amount": 2000,
        "task_id": "5",
        "5.1": {
            "task": "Task 5.1",
            "hours": 70,
            "unit_price": 400,
            "discount": 100,
            "amount": 2800,
            "task_id": "5.1",
        },
    },
    "6": {
        "task": "Task 6",
        "hours": 60,
        "unit_price": 150,
        "discount": 300,
        "amount": 3000,
        "task_id": "6",
        "6.1": {
            "task": "Task 6.1",
            "hours": 70,
            "unit_price": 150,
            "discount": 300,
            "amount": 2000,
            "task_id": "6.1",
            "6.1.1": {
                "task": "Task 6.1.1",
                "hours": 50,
                "unit_price": 150,
                "discount": 200,
                "amount": 1000,
                "task_id": "6.1.1",
            },
        },
        "6.2": {
            "task": "Task 6.2",
            "hours": 30,
            "unit_price": 200,
            "discount": 50,
            "amount": 3000,
            "task_id": "6.2",
        },
    },
    "7": {
        "task": "Task 7",
        "hours": 90,
        "unit_price": 300,
        "discount": 150,
        "amount": 12000,
        "task_id": "7",
    },
    "8": {
        "task": "Task 8",
        "hours": 110,
        "unit_price": 450,
        "discount": 200,
        "amount": 6000,
        "task_id": "8",
        "8.1": {
            "task": "Task 8.1",
            "hours": 25,
            "unit_price": 350,
            "discount": 75,
            "amount": 8000,
            "task_id": "8.1",
        },
    },
    "9": {
        "task": "Task 9",
        "hours": 20,
        "unit_price": 50,
        "discount": 15,
        "amount": 1000,
        "task_id": "9",
    },
    "10": {
        "task": "Task 10",
        "hours": 150,
        "unit_price": 200,
        "discount": 100,
        "amount": 12000,
        "task_id": "10",
    },
}


load_dotenv()
# Fetch environment variables
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")
database = os.getenv("POSTGRES_DB")

print(database, "------------------------")

pg_url = f"postgresql://{user}:{password}@{host}:{port}/invoicehandler"


engine = create_engine(pg_url)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Yield the correct session based on request type (write or read)."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def save_tasks(db):
    truncate_invoice_table(db)

    def save_invoice(key, item):
        create_invoice(
            db,
            key,
            item["task"],
            item["hours"],
            item["unit_price"],
            item["discount"],
            item["amount"],
        )
        extra_keys = get_extra_keys(item)
        for extra_key in extra_keys:
            nested_item = item[extra_key]
            save_invoice(extra_key, nested_item)

    for key, item in data.items():
        save_invoice(key, item)


def main():
    # Create a new database session
    db = next(get_db())
    try:
        save_tasks(db)
        print("Data seeded successfully!")
    except Exception as e:
        print(f"An error occurred while seeding data: {e}")
    finally:
        db.close()  # Ensure the session is closed after operation


if __name__ == "__main__":
    main()
