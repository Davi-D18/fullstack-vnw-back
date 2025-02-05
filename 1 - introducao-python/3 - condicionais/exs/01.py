# Simular um caixa eletrônico
import time

saldo_usuario = 500

def sacar():
  global saldo_usuario

  valor_para_sacar = int(input("Quanto deseja sacar? "))

  if (valor_para_sacar > saldo_usuario):
    print("Processando...")
    time.sleep(2)
    print("Erro, saldo insuficiente")
  else:
    print("Processando...")
    time.sleep(2)
    print(f"Sucesso! você acaba de sacar {valor_para_sacar}, seu saldo atual é de: {saldo_usuario}")

def depositar():
  global saldo_usuario

  valor_depositar = int(input("Quanto deseja depositar? "))
  print("Processando...")

  saldo_novo = valor_depositar + saldo_usuario
  saldo_usuario = saldo_novo

  time.sleep(2)
  print(f"Sucesso! Você acaba de depositar {valor_depositar}, seu saldo total é de: {saldo_usuario}")


print("Bem vindo ao Caixa")
print("1 - Sacar | 2 - Depositar | 0 - Sair")
acao_usuario = int(input("O que deseja fazer? "))

if acao_usuario == 1:
  sacar()
elif acao_usuario == 2:
  depositar()
else:
  print("Saindo do sistema...")