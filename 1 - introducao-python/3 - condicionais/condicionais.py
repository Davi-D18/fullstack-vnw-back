import os
import time

print("Bem vindo ao sistema(Condicional)")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
  print(f"{nome} você é maior de idade")
else:
  print(f"{nome} você é menor de idade")

time.sleep(1.5)
os.system('cls' if os.name == 'nt' else 'clear')

"""-------------------------------------------"""

# Ternário
print("Bem vindo ao sistema(Ternário)")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print("Você é maior de idade") if idade >= 18 else print("Você é menor de idade")

time.sleep(1.5)
os.system('cls' if os.name == 'nt' else 'clear')

"""-------------------------------------------"""

# Condicional Aninhada
print("Bem vindo ao sistema(Condicional Aninhada)")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
  print(f"{nome} você é maior de idade")
elif idade >= 65:
  print(f"{nome} você é idoso")
else:
  print(f"{nome} você é adulto")

# JavaScript --> &, ||, !
# Python --> and, or, not

# and (e) --> retorna um resultado verdadeiro, caso as duas perguntas sejam verdadeiras
# Eu quero sorvete e batata frita --> True/False

# or (ou) --> retorna um resultado verdadeiro, caso uma das duas perguntas seja verdadeira
# Eu quero sorvete ou batata frita --> True/False

# not (negação) --> inverte qualquer resultado, caso seja True retorna False, caso seja False retorna True

# Operadores de Comparação

# > -- Verifica se um valor é maior que outro
# < -- Verifica se um valor é menor que outro
# >= -- Verifica se um valor é maior ou igual a outro
# <= -- Verifica se um valor é menor ou igual a outro
# != -- Verifica se um valor é diferente de outro
# == -- Verifica se um valor é igual ao outro