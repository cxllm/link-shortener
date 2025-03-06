from db import connect


def execute():
    conn, cursor = connect()
    path = input("Enter the path of the shortened URL: ")
    if path.upper() == path:
        path = path.lower()
    exists = False
    while not exists:
        cursor.execute("SELECT * FROM links WHERE path = %s", (path,))
        if cursor.fetchone() is None:
            print("This path does not exist!")
            path = input("Enter a different path: ")
        else:
            exists = True
    cursor.execute("DELETE FROM links WHERE path = %s", (path,))
    conn.commit()
    conn.close()
