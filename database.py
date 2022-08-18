import sqlite3

DATABASE = 'users_db.sqlite'


def connect_to_db():
    conn = sqlite3.connect(DATABASE)
    return conn


def create_db_table():
    query = '''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY NOT NULL,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        address TEXT NOT NULL,
        phone TEXT NOT NULL
    );
    '''

    conn = connect_to_db()
    conn.execute(query)
    conn.commit()
    conn.close()
