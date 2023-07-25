```python
import sqlite3
from sqlite3 import Error

# Database Connection
def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:') # creates a database in RAM
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

# User Schema
def create_user_table(conn):
    try:
        sql_create_user_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        profile text,
                                        interactions text
                                    ); """
        c = conn.cursor()
        c.execute(sql_create_user_table)
    except Error as e:
        print(e)

# Content Schema
def create_content_table(conn):
    try:
        sql_create_content_table = """CREATE TABLE IF NOT EXISTS content (
                                    id integer PRIMARY KEY,
                                    text text NOT NULL,
                                    images text,
                                    videos text
                                );"""
        c = conn.cursor()
        c.execute(sql_create_content_table)
    except Error as e:
        print(e)

# Main function to setup the database
def main():
    conn = create_connection()

    if conn is not None:
        create_user_table(conn)
        create_content_table(conn)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
```