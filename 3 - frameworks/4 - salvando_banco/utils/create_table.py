import sqlite3


def create_table(query):
  with sqlite3.connect("./data/database.db") as conn:
      conn.execute(query)