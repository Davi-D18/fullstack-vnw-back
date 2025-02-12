# Manipulação de Strings

## 🔹 **Manipulação de Maiúsculas e Minúsculas**
- `s.lower()` → Converte todos os caracteres para minúsculas.  
- `s.upper()` → Converte todos os caracteres para maiúsculas.  
- `s.capitalize()` → Converte o primeiro caractere para maiúscula e o restante para minúsculas.  
- `s.title()` → Converte para o formato de título (primeira letra de cada palavra em maiúscula).  
- `s.swapcase()` → Inverte as letras maiúsculas e minúsculas.  

### **Exemplo**
```python
s = "python é incrível"
print(s.upper())      # "PYTHON É INCRÍVEL"
print(s.title())      # "Python É Incrível"
```

---

## 🔹 **Remoção de Espaços e Caracteres**
- `s.strip()` → Remove espaços em branco no início e no final.  
- `s.lstrip()` → Remove espaços à esquerda (início da string).  
- `s.rstrip()` → Remove espaços à direita (final da string).  

### **Exemplo**
```python
s = "   Olá Mundo!   "
print(s.strip())   # "Olá Mundo!"
```

---

## 🔹 **Substituição e Divisão**
- `s.replace("antigo", "novo")` → Substitui partes da string.  
- `s.split("separador")` → Divide a string em uma lista, usando um delimitador.  
- `'separador'.join(lista)` → Junta uma lista de strings em uma única string.  

### **Exemplo**
```python
s = "banana, maçã, laranja"
lista = s.split(", ")   # ['banana', 'maçã', 'laranja']
nova_string = " - ".join(lista)  # "banana - maçã - laranja"
```

---

## 🔹 **Verificação de Conteúdo**
- `s.startswith("prefixo")` → Retorna `True` se a string começar com o valor informado.  
- `s.endswith("sufixo")` → Retorna `True` se a string terminar com o valor informado.  
- `s.isalpha()` → Retorna `True` se a string contém apenas letras.  
- `s.isdigit()` → Retorna `True` se a string contém apenas números.  
- `s.isalnum()` → Retorna `True` se a string contém apenas letras e números (sem espaços ou símbolos).  
- `s.isspace()` → Retorna `True` se a string contém apenas espaços em branco.  

### **Exemplo**
```python
s = "Python"
print(s.isalpha())  # True
print(s.isdigit())  # False
```

---

## 🔹 **Formatação de Strings**
- `s.zfill(tamanho)` → Preenche a string com zeros à esquerda até atingir o tamanho especificado.  
- `s.center(tamanho, "caractere")` → Centraliza a string preenchendo com o caractere especificado.  
- `s.ljust(tamanho, "caractere")` → Alinha à esquerda.  
- `s.rjust(tamanho, "caractere")` → Alinha à direita.  
- `f"texto {variavel}"` → Formatação moderna usando `f-strings`.  

### **Exemplo**
```python
numero = "42"
print(numero.zfill(5))  # "00042"

nome = "Python"
print(nome.center(10, "-"))  # "--Python--"
```

---

## 🔹 **Busca em Strings**
- `s.find("texto")` → Retorna o índice da primeira ocorrência da substring ou `-1` se não for encontrada.  
- `s.rfind("texto")` → Retorna o índice da última ocorrência.  
- `s.count("texto")` → Conta quantas vezes uma substring aparece na string.  

### **Exemplo**
```python
s = "banana"
print(s.find("na"))   # 2
print(s.count("a"))   # 3
```

----------------------------------------------------------------------------------

# Loops
Os **loops** em Python permitem repetir ações sem precisar escrever várias vezes o mesmo código. 

# 🔹 **Tipos de Loops em Python**  

## 🔸 **1️⃣ `for` – Percorre itens de uma sequência**  
O loop `for` é usado para percorrer **listas, strings, tuplas, dicionários** e até mesmo **números** com `range()`. Ele repete um bloco de código **para cada item** da sequência.

### **📌 Exemplo com listas**  
```python
nomes = ["Ana", "Carlos", "Bruna"]

for nome in nomes:
    print(f"Olá, {nome}!")
```
🔹 **Saída:**  
```
Olá, Ana!  
Olá, Carlos!  
Olá, Bruna!  
```
Aqui, o loop pega **cada nome** da lista e imprime uma saudação.

---

### **📌 Exemplo com strings**  
As strings são **coleções de caracteres**, então podemos percorrer letra por letra.

```python
palavra = "Python"

for letra in palavra:
    print(letra)
```
🔹 **Saída:**  
```
P  
y  
t  
h  
o  
n  
```

---

### **📌 Exemplo com `range()` (números sequenciais)**  
A função `range(início, fim, passo)` gera uma sequência de números.  
- **O "fim" não é incluído!**  
- O **passo** é opcional (padrão é `1`).  

```python
for i in range(1, 6):  # Vai de 1 até 5
    print(f"Número: {i}")
```
🔹 **Saída:**  
```
Número: 1  
Número: 2  
Número: 3  
Número: 4  
Número: 5  
```

💡 **Dicas com `range()`:**  
```python
print(list(range(5)))       # [0, 1, 2, 3, 4]  (Começa em 0 por padrão)
print(list(range(2, 10, 2)))  # [2, 4, 6, 8]  (Vai de 2 até 8, pulando de 2 em 2)
```

---

### **📌 Exemplo com dicionários**  
Podemos percorrer **somente as chaves**, **somente os valores** ou **chaves e valores juntos**.

```python
dados = {"nome": "Ana", "idade": 25}

for chave, valor in dados.items():
    print(f"{chave}: {valor}")
```
🔹 **Saída:**  
```
nome: Ana  
idade: 25  
```

💡 **Outras formas de percorrer dicionários:**  
```python
for chave in dados.keys():  # Apenas as chaves
    print(chave)

for valor in dados.values():  # Apenas os valores
    print(valor)
```

---

## 🔸 **2️⃣ `while` – Repete enquanto a condição for verdadeira**  
O `while` repete um bloco **enquanto uma condição for `True`**.  
**Cuidado para não criar loops infinitos!** Sempre lembre de atualizar a condição dentro do loop.  

### **📌 Exemplo de contagem**  
```python
contador = 1

while contador <= 5:  # Continua enquanto for menor ou igual a 5
    print(f"Número: {contador}")
    contador += 1  # Importante atualizar o valor!
```
🔹 **Saída:**  
```
Número: 1  
Número: 2  
Número: 3  
Número: 4  
Número: 5  
```

---

### **📌 Exemplo pedindo entrada do usuário**  
Aqui o programa continua rodando até que o usuário digite `"sair"`.

```python
comando = ""

while comando != "sair":
    comando = input("Digite um comando (ou 'sair' para parar): ")
    print(f"Você digitou: {comando}")
```
🔹 **Saída (depende do que o usuário digitar):**  
```
Digite um comando (ou 'sair' para parar): oi
Você digitou: oi
Digite um comando (ou 'sair' para parar): teste
Você digitou: teste
Digite um comando (ou 'sair' para parar): sair
Você digitou: sair
```

---

## 🔹 **Controlando Loops (`break` e `continue`)**  

### **📌 `break` – Interrompe o loop imediatamente**  
Se `break` for encontrado, o loop **para na hora**, mesmo que ainda tenha mais itens para percorrer.

```python
for numero in range(1, 10):
    if numero == 5:
        break  # Sai do loop quando numero for 5
    print(numero)
```
🔹 **Saída:**  
```
1  
2  
3  
4  
```

---

### **📌 `continue` – Pula para a próxima iteração**  
Se `continue` for encontrado, o loop **ignora o código abaixo** dele e volta para o início.

```python
for numero in range(1, 6):
    if numero == 3:
        continue  # Pula o número 3
    print(numero)
```
🔹 **Saída:**  
```
1  
2  
4  
5  
```

---

## 🔹 **Usando `enumerate()` para pegar índice e valor**  
O `enumerate(lista)` retorna **o índice e o valor** de cada item.  

```python
nomes = ["Ana", "Carlos", "Bruna"]

for indice, nome in enumerate(nomes):
    print(f"{indice}: {nome}")
```
🔹 **Saída:**  
```
0: Ana  
1: Carlos  
2: Bruna  
```

---

## 🔹 **Usando `zip()` para percorrer duas listas ao mesmo tempo**  
Se tivermos duas listas, podemos percorrê-las ao mesmo tempo com `zip()`.

```python
nomes = ["Ana", "Carlos", "Bruna"]
idades = [25, 30, 22]

for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos.")
```
🔹 **Saída:**  
```
Ana tem 25 anos.  
Carlos tem 30 anos.  
Bruna tem 22 anos.  
```

---

## 🎯 **Resumo**
| Comando | O que faz? |
|---------|-----------|
| `for` | Percorre itens de uma sequência (lista, string, etc.). |
| `while` | Repete um bloco **enquanto** a condição for verdadeira. |
| `break` | Sai do loop imediatamente. |
| `continue` | Pula para a próxima repetição do loop. |
| `enumerate(lista)` | Pega o índice e o valor ao mesmo tempo. |
| `zip(lista1, lista2)` | Percorre duas listas ao mesmo tempo. |