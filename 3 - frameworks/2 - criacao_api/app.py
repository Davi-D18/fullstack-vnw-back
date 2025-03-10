from flask import Flask, json

from functions import funcao_teste

app = Flask(__name__)

@app.route("/")
def view():
  return json.jsonify({"message": "Tudo funcionando :)!"})

@app.route("/teste")
def teste():
  return json.jsonify({"message": "Rota funcionando :)"})

@app.route("/teste2")
def teste2():
  return funcao_teste()

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)