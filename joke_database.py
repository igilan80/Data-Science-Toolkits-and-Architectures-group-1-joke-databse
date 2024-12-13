import psycopg2

# Database connection settings
HOST = "localhost"
PORT = 5432
USER = "admin"
PASSWORD = "admin"
DB_NAME = "testdb"

def connect_to_database():
    """Connect to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            host=HOST, port=PORT, user=USER, password=PASSWORD, database=DB_NAME
        )
        print("Connected to the database successfully.")
        return conn
    except Exception as e:
        print("Error connecting to the database:", e)
        exit()

def create_jokes_table():
    """Create the 'jokes' table if it doesn't exist."""
    conn = connect_to_database()
    cur = conn.cursor()
    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS jokes (
                ID SERIAL PRIMARY KEY,
                JOKE TEXT NOT NULL
            );
        """)
        conn.commit()
        print("Table 'jokes' created.")
    except Exception as e:
        print("Error creating table:", e)
    finally:
        cur.close()
        conn.close()

def add_joke(joke):
    """Insert a joke into the jokes table."""
    conn = connect_to_database()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO jokes (JOKE) VALUES (%s) RETURNING ID;", (joke,))
        joke_id = cur.fetchone()[0]
        conn.commit()
        print(f"Joke added with ID: {joke_id}")
    except Exception as e:
        print("Error adding joke:", e)
    finally:
        cur.close()
        conn.close()

def fetch_all_jokes():
    """Retrieve all jokes from the jokes table."""
    conn = connect_to_database()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM jokes;")
        jokes = cur.fetchall()
        for joke in jokes:
            print(f"ID: {joke[0]}, Joke: {joke[1]}")
    except Exception as e:
        print("Error fetching jokes:", e)
    finally:
        cur.close()
        conn.close()

# Main script
if __name__ == "__main__":
    create_jokes_table()
    add_joke("Why don't scientists trust atoms? Because they make up everything!")
    print("Current jokes in the database:")
    fetch_all_jokes()

