Algumas informações antes de fazer Deploy

# Same Origin Policy
Por padrão, nas APIs não permite sites de diferentes dominios acessarem a API, por isso precisa configurar o **CORS**.

## Configurando

1. Instale o **flask-cors** e o **gunicorn**
```py
pip install flask-cors gunicorn
```

2. No arquivo principal onde inicializa a aplicação, adicione:
```py
from flask_cors import CORS
from flask import Flask

app = Flask(__name__)

CORS(app)
```

3. Atualize as depêndencias
```shell
pip freeze > requirements.txt
```

4. Execute o comando abaixo para testar se está funcionando
    
    gunicorn arquivo_principal:variavel_armazenado_instancia_flask

```shell
gunicorn app:app
```