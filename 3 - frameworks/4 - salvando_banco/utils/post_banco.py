import sqlite3


def post_banco(livro):
    with sqlite3.connect("./data/database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO livros(titulo, categoria, autor, imagem_url)
            VALUES(?, ?, ?, ?)
            """,
            (livro['titulo'], livro['categoria'], livro['autor'], livro['imagem_url'])
        )

        return {"message": "Livro cadastrado com sucesso!"}