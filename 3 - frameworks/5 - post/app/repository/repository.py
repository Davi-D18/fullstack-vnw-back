import sqlite3

database = "app/data/data.db"
def criar_tabela():
  try:
    with sqlite3.connect(f"{database}") as conn:
      cursor = conn.cursor()
      cursor.execute(
        "CREATE TABLE IF NOT EXISTS livros (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, categoria TEXT, autor TEXT, image_url TEXT)"
      )
      conn.commit()
      return True
  except sqlite3.Error as e:
    print(f"Erro ao criar a tabela: {e}")
    return False
  
def inserir_dados(titulo, categoria, autor, image_url):
  try:
    with sqlite3.connect(f"{database}") as conn:
      cursor = conn.cursor()
      cursor.execute(
        "INSERT INTO livros (titulo, categoria, autor, image_url) VALUES (?, ?, ?, ?)",
        (titulo, categoria, autor, image_url),
      )
      conn.commit()
      return True
  except sqlite3.Error as e:
    print(f"Erro ao inserir dados: {e}")
    return False