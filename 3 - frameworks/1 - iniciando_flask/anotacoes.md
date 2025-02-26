## 1. Introdução

- **Flask** é um microframework para desenvolvimento web em Python.
- Focado em simplicidade e flexibilidade, permitindo criar desde pequenos sites até APIs RESTful.
- Baseia-se em três componentes principais:
  - **Werkzeug:** Ferramenta WSGI para manipulação de requisições e respostas.
  - **Jinja2:** Motor de templates para renderizar HTML.
  - **Click:** Biblioteca para criação de interfaces de linha de comando.

---

## 2. Instalação e Configuração

### Instalação

- Instale o Flask usando o pip:
  ```bash
  pip install flask
  ```

### Configuração Básica

- Crie um arquivo (por exemplo, `app.py`) e importe a classe `Flask`:
  ```python
  from flask import Flask

  app = Flask(__name__)
  ```
- Configure variáveis de ambiente ou use arquivos de configuração (ex.: `config.py`) para separar ambientes de desenvolvimento, testes e produção.

---

## 3. Como Usar o Flask

### Estrutura da Aplicação

- **Instância da aplicação:** É o objeto central que gerencia rotas, configurações e contextos.
- **Contextos:**
  - **Application Context:** Permite acessar `current_app` e armazenar variáveis globais.
  - **Request Context:** Disponibiliza o objeto `request` com dados da requisição (método, parâmetros, etc.).

### Organização de Diretórios

- Para projetos maiores, recomenda-se organizar a aplicação em pacotes:
  ```
  meu_projeto/
  ├── app.py
  ├── config.py
  ├── templates/
  ├── static/
  └── blueprints/
      └── usuarios.py
  ```
- **Blueprints:** Módulos que permitem separar rotas e funcionalidades em arquivos distintos.

---

## 4. Como Criar Rotas

### Rotas Básicas

- Utilize o decorator `@app.route` para definir rotas:
  ```python
  @app.route("/")
  def index():
      return "Olá, mundo!"
  ```

### Rotas Dinâmicas

- Defina rotas com parâmetros variáveis:
  ```python
  @app.route("/usuario/<int:id>")
  def usuario(id):
      return f"Usuário com ID {id}"
  ```
- O trecho `<int:id>` indica que o Flask deve converter o valor da URL para inteiro.

### Métodos HTTP

- Por padrão, as rotas respondem a requisições GET. Para outros métodos, especifique com o argumento `methods`:
  ```python
  @app.route("/usuarios", methods=["POST"])
  def criar_usuario():
      # Obter dados com request.get_json() ou request.form
      return "Usuário criado", 201
  ```

---

## 5. Como Rodar a Aplicação

### Modo de Desenvolvimento

- Dentro do próprio código, use:
  ```python
  if __name__ == "__main__":
      app.run(debug=True)
  ```
  - `debug=True` ativa o modo debug (recarregamento automático e debugger).
  
### Linha de Comando com Flask CLI

- Configure a variável de ambiente `FLASK_APP` e rode com o comando:
  ```bash
  export FLASK_APP=app.py   # No Linux/Mac
  set FLASK_APP=app.py      # No Windows
  flask run
  ```
- O comando `flask run` inicia o servidor de desenvolvimento do Flask.

### Considerações de Deploy

- Para produção, recomenda-se utilizar servidores WSGI (como Gunicorn ou uWSGI) e desativar o modo debug.

---

## 6. Exemplos Práticos

### Exemplo Completo de `app.py`

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota básica
@app.route("/")
def index():
    return "Olá, mundo!"

# Rota dinâmica
@app.route("/usuario/<int:id>")
def usuario(id):
    return jsonify({"mensagem": f"Usuário com ID {id}"})

# Rota com método POST
@app.route("/usuarios", methods=["POST"])
def criar_usuario():
    dados = request.get_json()
    # Aqui você processaria os dados recebidos
    return jsonify({"mensagem": "Usuário criado", "dados": dados}), 201

if __name__ == "__main__":
    app.run(debug=True)
```

### Uso de Blueprints (para Modularização)

- **Arquivo:** `blueprints/usuarios.py`
  ```python
  from flask import Blueprint, jsonify

  usuarios_bp = Blueprint('usuarios', __name__)

  @usuarios_bp.route("/", methods=["GET"])
  def listar_usuarios():
      # Lógica para listar usuários
      return jsonify({"usuarios": []})
  ```
- **Registro no arquivo principal (`app.py`):**
  ```python
  from flask import Flask
  from blueprints.usuarios import usuarios_bp

  app = Flask(__name__)
  app.register_blueprint(usuarios_bp, url_prefix="/usuarios")

  if __name__ == "__main__":
      app.run(debug=True)
  ```

---

## Resumo

- **Instalação:** `pip install flask`
- **Configuração:** Crie uma instância de Flask e configure variáveis conforme o ambiente.
- **Rotas:** Utilize `@app.route` para mapear URLs para funções que retornam respostas.
- **Execução:** Rode a aplicação via `app.run(debug=True)` ou pelo CLI com `flask run`.
- **Modularização:** Para aplicações maiores, use Blueprints e organize os arquivos em pastas (templates, static, blueprints).