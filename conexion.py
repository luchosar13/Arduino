import psycopg2
import contextlib

db_params = dict(
    host="localhost",
    database="postgres",
    port=5432,
    user="postgres",
    password="abcd1234"
)

def conect_to_db(db_params):
    print("Connecting to PostgreSQL database...")
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()

    cur.close()
    conn.close()

@contextlib.contextmanager

def database(params):
    print("Connecting to PostgreSQL database...")
    # Setup script
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    try:
        yield cur
    finally:
        # Teardown script
        cur.close()
        conn.commit()
        conn.close()
        print("Database connection closed.")
