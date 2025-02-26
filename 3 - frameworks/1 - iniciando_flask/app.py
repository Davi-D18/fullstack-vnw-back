from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados simulados
usuarios = [
    {"id": 1, "nome": "Alice", "email": "alice@example.com"},
    {"id": 2, "nome": "Bob", "email": "bob@example.com"}
]

# Rota inicial
@app.route("/", methods=["GET"])
def index():
    return "<h1>API de Usuários</h1>"

# Listar todos os usuários
@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios), 200

# Obter um usuário específico
@app.route("/usuarios/<int:id>", methods=["GET"])
def obter_usuario(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if usuario:
        return jsonify(usuario), 200
        # jsonify -> converte o dicionário para JSON

    return jsonify({"mensagem": "Usuário não encontrado"}), 404

# Criar um novo usuário
@app.route("/usuarios", methods=["POST"])
def criar_usuario():
    dados = request.get_json()
    novo_usuario = {
        "id": len(usuarios) + 1,
        "nome": dados.get("nome"),
        "email": dados.get("email")
    }
    usuarios.append(novo_usuario)
    return jsonify(novo_usuario), 201

# Atualizar um usuário existente
@app.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if not usuario:
        return jsonify({"mensagem": "Usuário não encontrado"}), 404
    dados = request.get_json()
    usuario["nome"] = dados.get("nome", usuario["nome"])
    usuario["email"] = dados.get("email", usuario["email"])
    return jsonify(usuario), 200

# Deletar um usuário
@app.route("/usuarios/<int:id>", methods=["DELETE"])
def deletar_usuario(id):
    global usuarios
    usuarios = [u for u in usuarios if u["id"] != id]
    return jsonify({"mensagem": "Usuário deletado"}), 200

if __name__ == "__main__":
    app.run(debug=True)
