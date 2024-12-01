import psycopg2
from psycopg2 import OperationalError

def test_connection():
    try:
        conn = psycopg2.connect(
            host="db",  # Or "db" if running from another container
            user="postgres",
            password="clocotest",
            dbname="invoice-handler",
            port=5432
        )
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("PostgreSQL version:", db_version)
        cursor.close()
        conn.close()
    except OperationalError as e:
        print(f"Error: {e}")
        
# Run the test
test_connection()
