import sqlite3

from flask import jsonify


def get_banco():
    with sqlite3.connect("./data/database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM livros")
        rows = cursor.fetchall()
        
        # Converte os resultados em uma lista de dicionários
        colunas = [col[0] for col in cursor.description]  # Nomes das colunas
        dados = [dict(zip(colunas, row)) for row in rows]
    return jsonify(dados)