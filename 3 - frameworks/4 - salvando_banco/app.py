from flask import Flask, json, request

from utils import create_table, get_banco, post_banco

app = Flask(__name__)

@app.route("/")
def view():
  return json.jsonify({"message": "Tudo funcionando :)!"})

@app.route("/doar", methods=["POST"])
def cadastrar_livro():
  dados = request.get_json() # Pega os dados enviados pelo usuário
  return post_banco(dados)

@app.route("/livros", methods=["GET"])
def listar_livros():
  return get_banco()

@app.route("/init", methods=["POST"])
def init_db():
  query = request.get_json()
  return create_table(query)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)