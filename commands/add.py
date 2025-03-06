from db import connect


def execute():
    conn, cursor = connect()
    path = input("Enter the path of the shortened URL: ")
    if path.upper() == path:
        path = path.lower()
    exists = True
    while exists:
        cursor.execute("SELECT * FROM links WHERE path = %s", (path,))
        if cursor.fetchone() is not None:
            print("This path is already in use!")
            path = input("Enter a different path: ")
        else:
            exists = False
    destination = input("Enter the destination: ")
    name = input("Enter the name: ")
    cursor.execute("INSERT INTO links VALUES (%s, %s, %s)", (path, destination, name))
    conn.commit()
    conn.close()
