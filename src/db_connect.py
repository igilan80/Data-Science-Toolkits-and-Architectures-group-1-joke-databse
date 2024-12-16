import os
import psycopg2
from psycopg2 import OperationalError
import time


def connect(retries=5, delay=5):
    for attempt in range(retries):
        try:
            return psycopg2.connect(
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT")
            )
        except OperationalError as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
    raise OperationalError(
        "Failed to connect to the database after multiple attempts.")
