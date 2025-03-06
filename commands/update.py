from db import connect


def execute():
    conn, cursor = connect()
    path = input("Enter the path of the shortened URL: ")
    if path.upper() == path:
        path = path.lower()
    exists = False
    data = ()
    while not exists:
        cursor.execute("SELECT * FROM links WHERE path = %s", (path,))
        data = cursor.fetchone()
        if data is None:
            print("This path does not exist!")
            path = input("Enter a different path: ")
        else:
            exists = True
    _, prev_d, prev_n = data
    destination = input("Enter the updated destination (leave blank for the same): ")
    if destination == "":
        destination = prev_d
    name = input("Enter the updated name (leave blank for same): ")
    if name == "":
        name = prev_n
    if name != prev_n or destination != prev_d:
        cursor.execute(
            "UPDATE links SET destination = %s, name = %s WHERE path = %s",
            (destination, name, path),
        )
    conn.commit()
    conn.close()
