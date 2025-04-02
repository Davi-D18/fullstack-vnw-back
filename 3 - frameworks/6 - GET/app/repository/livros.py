import sqlite3


def connect():
  conn = sqlite3.connect('app/database/data.db')
  return conn

def criar_tabela():
  conn = connect()
  try:
    conn.execute("""
                 CREATE TABLE IF NOT EXISTS livros (
                 id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 titulo TEXT, 
                 categoria TEXT, 
                 autor TEXT, 
                 image_url TEXT)
                 """)
    conn.commit()
    return True
  except sqlite3.OperationalError:
    return False

def obter_livros():
  conn = connect()
  tabela_criada = criar_tabela()

  if not tabela_criada:
    return

  livros = conn.execute("SELECT * FROM livros").fetchall()

  livros_formatados = []

  for item in livros:
    dicionario_livro = {
      "id": item[0],
      "titulo": item[1],
      "categoria": item[2],
      "autor": item[3],
      "image_url": item[4]
    }
    livros_formatados.append(dicionario_livro)

  return livros_formatados