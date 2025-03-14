import sqlite3

from flask import Flask, json

app = Flask(__name__)

@app.route("/")
def view():
  return json.jsonify({"message": "Tudo funcionando :)!"})

def init_db():
    with sqlite3.connect("./data/database.db") as conn:
       conn.execute(
            """
            CREATE TABLE IF NOT EXISTS livros(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                categoria TEXT NOT NULL,
                autor TEXT NOT NULL,
                imagem_url TEXT NOT NULL
            )
            """
        )

init_db()

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)