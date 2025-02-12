# Definindo uma tupla
tupla = ("a", "b", "c", "d", "e")

# Acessando elementos da tupla
print("Primeiro elemento:", tupla[0])
print("Segundo elemento:", tupla[1])

# Fatiando a tupla
print("Elementos do índice 1 ao 3 (exclusivo):", tupla[1:3])

# Tentando modificar um elemento da tupla (isso causará um erro, pois tuplas são imutáveis)
try:
  tupla[0] = "z"
except TypeError as e:
  print("Erro ao tentar modificar a tupla:", e)

# Iterando sobre os elementos da tupla
print("Iterando sobre a tupla:")
for elemento in tupla:
  print(elemento)

# Verificando se um elemento está na tupla
print("O elemento 'a' está na tupla?", "a" in tupla)
print("O elemento 'z' está na tupla?", "z" in tupla)

# Obtendo o comprimento da tupla
print("Comprimento da tupla:", len(tupla))

# Concatenando duas tuplas
outra_tupla = ("f", "g")
tupla_concatenada = tupla + outra_tupla
print("Tupla concatenada:", tupla_concatenada)

# Desempacotando a tupla
a, b, c, d, e = tupla
print("Desempacotando a tupla:", a, b, c, d, e)
