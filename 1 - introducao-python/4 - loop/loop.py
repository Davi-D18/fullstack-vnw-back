import os
import time

# Aula sobre loops

# While

numero_final = 1

while numero_final <= 10:
  print("Hello")
  numero_final += 1


# For -> É mais usado para percorrer informações

os.system('cls' if os.name == 'nt' else 'clear')

Dados = [
  {
    "nome": "Davi",
    "idade": 19
  },
  {
    "nome": "Lucas",
    "idade": 25
  },
  {
    "nome": "Tiago",
    "idade": 30
  },
  {
    "nome": "Marcos",
    "idade": 33
  }
]

for dado in Dados:
  print(f"Olá, sou o {dado['nome']} e tenho {dado['idade']}")


time.sleep(2)

nomes = ["João", "Mara", "Maria"]

for nome in nomes:
  print(nome)