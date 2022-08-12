import sqlite3


def connect_to_db():
    conn = sqlite3.connect('users_db.sqlite')
    return conn


def create_db_table():
    conn = connect_to_db()
    conn.execute('''
        CREATE TABLE users (
            user_id INTEGER PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            address TEXT NOT NULL,
            phone TEXT NOT NULL
        );
    ''')
    conn.commit()
    conn.close()


# create_db_table()
