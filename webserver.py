from flask import Flask, redirect, request
from db import connect

app = Flask(__name__)


@app.get("/")
def root():
    return redirect("https://www.cxllm.uk/")


@app.errorhandler(404)
def handler(_):
    path = request.path[1:].lower()
    conn, cursor = connect()
    cursor.execute("SELECT destination FROM links WHERE path = %s", (path,))
    url = cursor.fetchone()
    conn.close()
    if url is None:
        return "404"
    else:
        return redirect(url[0])


if __name__ == "__main__":
    app.run(port=3000, debug=True)
