from flask import Flask, json

from app.repository.livros import obter_livros

app = Flask(__name__)

@app.route("/livros", methods=["GET"])
def livros():
  livros = obter_livros()
  return json.dumps(livros, sort_keys=False) # sort_keys=False desabilita a ordenação dos campos

if __name__ == "__main__":
  app.run(port=5000, debug=True)