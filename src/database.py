"""
    This module is used to create a database connection using sqlalchemy
"""

import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session

# Load environment variables for Postgres connections

# Fetch environment variables
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")
database = os.getenv("POSTGRES_DB")

pg_url = f"postgresql://{user}:{password}@{host}:{port}/{database}"


engine = create_engine(pg_url)


# Test the connection
# try:
#     with engine.connect() as connection:
#         result = connection.execute(text("SELECT version();"))
#         version = result.fetchone()
#         print("Connection successful! PostgreSQL version:", version[0])
# except Exception as e:
#     print("Connection failed:", e)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Yield the correct session based on request type (write or read)."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_invoice_table(db: Session):
    db = next(db)
    # Check if the table exists
    result = db.execute(
        text(
            """
        SELECT EXISTS (
            SELECT 1
            FROM information_schema.tables 
            WHERE table_name='invoices'
        );
    """
        )
    )

    # Fetch the result
    table_exists = result.scalar()

    # Create the table if it doesn't exist
    if not table_exists:
        db.execute(
            text(
                """
        CREATE TABLE invoices (
            task_id VARCHAR PRIMARY KEY,
            task VARCHAR NOT NULL,
            hours INT NOT NULL,
            amount INT NOT NULL,
            discount INT NOT NULL,
            unit_price INT NOT NULL
        );
        """
            )
        )
        db.commit()


def create_task_table(db: Session):
    db = next(db)
    # Check if the table exists
    result = db.execute(
        text(
            """
        SELECT EXISTS (
            SELECT 1
            FROM information_schema.tables 
            WHERE table_name='tasks'
        );
    """
        )
    )

    # Fetch the result
    table_exists = result.scalar()

    # Create the table if it doesn't exist
    if not table_exists:
        db.execute(
            text(
                """
        CREATE TABLE tasks (
            task_id VARCHAR PRIMARY KEY,
            parents VARCHAR[]
        );
        """
            )
        )
        db.commit()


if __name__ == "__main__":
    create_invoice_table(get_db())
    create_task_table(get_db())
