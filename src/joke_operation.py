import pyjokes
from db_connect import connect


def execute_query(query, params=None, fetch=False):
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute(query, params)
        result = cur.fetchall() if fetch else None
        conn.commit()
        return result
    except Exception as e:
        print(f"Error executing query: {e}")
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()


def create_joke_table():
    query = """
        CREATE TABLE IF NOT EXISTS jokes (
            id SERIAL PRIMARY KEY,
            joke TEXT NOT NULL
        );
    """
    execute_query(query)


def add_joke(joke):
    query = "INSERT INTO jokes (joke) VALUES (%s) RETURNING id;"
    result = execute_query(query, (joke,), fetch=True)
    return result[0][0] if result else None


def delete_joke(joke_id):
    query = "DELETE FROM jokes WHERE id = %s;"
    execute_query(query, (joke_id,))


def get_all_jokes():
    query = "SELECT * FROM jokes;"
    return execute_query(query, fetch=True)


def modify_joke(joke_id, new_joke):
    query = "UPDATE jokes SET joke = %s WHERE id = %s;"
    execute_query(query, (new_joke, joke_id))


def get_random_jokes(count):
    return [pyjokes.get_joke() for _ in range(count)]
