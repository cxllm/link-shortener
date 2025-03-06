from db import connect


def execute():
    conn, cursor = connect()

    cursor.execute("SELECT * FROM links")
    links = cursor.fetchall()
    print_format = "| {:35}| {:20}| {:30}"
    print(print_format.format("Name", "Path", "Destination"))
    print("-" * 92)
    for path, destination, name in links:
        print(print_format.format(name, "/" + path, destination))
    conn.close()
