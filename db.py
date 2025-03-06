import os
import dotenv
import psycopg2


def connect():
    dotenv.load_dotenv()
    host = os.getenv("HOST")
    port = os.getenv("PORT")
    user = os.getenv("USER")
    dbname = os.getenv("DB")
    password = os.getenv("PASSWORD")
    conn = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password,
    )
    cursor = conn.cursor()

    return conn, cursor


def setup():
    conn, cursor = connect()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS links (
            PRIMARY KEY (path),
            path TEXT NOT NULL,
            destination TEXT NOT NULL,
            name TEXT NOT NULL
    )"""
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    setup()
