from flask import Flask, json, request

from app.services import inserir_informacoes

app = Flask(__name__)

@app.route("/doar", methods=["POST"])
def view():
  data = request.get_json()
  titulo = data.get("titulo")
  categoria = data.get("categoria")
  autor = data.get("autor")
  image_url = data.get("image_url")

  if not titulo or not categoria or not autor or not image_url:
    return json.dumps({"message": "Todos os campos são obrigatórios"}), 400

  return inserir_informacoes(titulo, categoria, autor, image_url)
if __name__ == "__main__":
  app.run(port=5000, debug=True)