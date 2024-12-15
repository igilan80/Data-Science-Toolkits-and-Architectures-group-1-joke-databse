import psycopg2

# Connect to the default database
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="mysecretpassword"
)
conn.autocommit = True  # Disable transaction mode for CREATE DATABASE
cur = conn.cursor()

# Create a new database
cur.execute("CREATE DATABASE ms3_jokes;")

# Close the connection to the default database
cur.close()
conn.close()

# Connect to the newly created database
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="ms3_jokes",
    user="postgres",
    password="mysecretpassword"
)
cur = conn.cursor()

# Create a table
cur.execute("CREATE TABLE jokes (id SERIAL PRIMARY KEY, joke TEXT);")
conn.commit()

# Insert a joke
cur.execute("INSERT INTO jokes (joke) VALUES (%s) RETURNING id;", ("Why did the scarecrow win an award? Because he was outstanding in his field!",))
joke_id = cur.fetchone()[0]
conn.commit()

# Retrieve and print the joke
cur.execute("SELECT joke FROM jokes WHERE id = %s;", (joke_id,))
print("Joke from DB:", cur.fetchone()[0])

# Close the connection
cur.close()
conn.close()

