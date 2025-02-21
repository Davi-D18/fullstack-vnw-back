import os
import time

clientes = {
  1: {
    'nome': 'João Silva',
    'idade': 28,
    'email': 'joao.silva@example.com'
  },
  2: {
    'nome': 'Maria Oliveira',
    'idade': 34,
    'email': 'maria.oliveira@example.com'
  },
  3: {
    'nome': 'Carlos Souza',
    'idade': 45,
    'email': 'carlos.souza@example.com'
  },
  4: {
    'nome': 'Aline Ferreira',
    'idade': 30,
    'email': 'aline.ferreira@example.com'
  }
}

cliente_id = 1
print(f"Nome: {clientes[cliente_id]['nome']}")
print(f"Idade: {clientes[cliente_id]['idade']}")
print(f"Email: {clientes[cliente_id]['email']}")

time.sleep(2)

comando = 'cls' if os.name == 'nt' else 'clear'

# if os.name == 'nt':
#   os.system('cls')
# else:
#   os.system('clear')

os.system(comando)

for cliente_id in clientes:
  print(f"Nome: {clientes[cliente_id]['nome']}")
  print(f"Idade: {clientes[cliente_id]['idade']}")
  print(f"Email: {clientes[cliente_id]['email']}")
  print('----------------------------------------')
  time.sleep(1)


del clientes[4] # Deletando um item do dicionário
print("Deletando um item do dicionário")
print("--------------------------------")

# -----------------------------------------

pessoas = {
  'João': 28,
  'Maria': 34,
  'Carlos': 45,
  'Aline': 30,
  'varias_pessoas': ["João", "Maria", "Carlos", "Aline"]
}

pessoas['varias_pessoas'].append("Fernando")

print(pessoas)

