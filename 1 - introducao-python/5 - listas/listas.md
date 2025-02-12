# **Listas e Tuplas em Python**

## **1. Listas (`list`)**
As listas em Python são **mutáveis**, ou seja, seus elementos podem ser alterados após a criação. São representadas por colchetes `[]`.

### **Criação de listas**
```python
# Lista vazia
a = []

# Lista com elementos
b = [1, 2, 3, 4, 5]

# Lista mista
c = [1, "Python", 3.14, True]

# Lista aninhada
d = [[1, 2, 3], [4, 5, 6]]
```

### **Principais métodos das listas:**

| Método | Descrição | Exemplo |
|--------|----------|---------|
| `append(item)` | Adiciona um item ao final da lista. | `lista.append(10)` |
| `insert(pos, item)` | Insere um item em uma posição específica. | `lista.insert(1, 20)` |
| `extend(iterável)` | Adiciona vários elementos de um iterável no final da lista. | `lista.extend([30, 40])` |
| `pop(pos)` | Remove e retorna o item da posição informada (padrão: último). | `item = lista.pop(2)` |
| `remove(item)` | Remove a primeira ocorrência do item na lista. | `lista.remove(10)` |
| `index(item, início, fim)` | Retorna o índice da primeira ocorrência de um item. | `lista.index(20)` |
| `count(item)` | Retorna a quantidade de vezes que o item aparece na lista. | `lista.count(10)` |
| `reverse()` | Inverte a ordem da lista. | `lista.reverse()` |
| `sort(key=None, reverse=False)` | Ordena a lista (padrão: crescente). Pode usar uma chave para ordenação. | `lista.sort(reverse=True)` |
| `copy()` | Retorna uma cópia da lista. | `copia = lista.copy()` |
| `clear()` | Remove todos os itens da lista. | `lista.clear()` |

### **Exemplo prático de manipulação de listas:**
```python
numeros = [5, 3, 8, 1, 9]
numeros.append(4)      # Adiciona 4 ao final da lista
numeros.insert(2, 10)  # Insere 10 na posição 2
numeros.sort()         # Ordena a lista
print(numeros)         # Saída: [1, 3, 4, 5, 8, 9, 10]
```

---

## **2. Tuplas (`tuple`)**
As tuplas são **imutáveis**, ou seja, seus elementos não podem ser alterados após a criação. São representadas por **parênteses `()`**.

### **Criação de tuplas**
```python
# Tupla vazia
a = ()

# Tupla com elementos
b = (1, 2, 3, 4, 5)

# Tupla mista
c = (1, "Python", 3.14, True)

# Tupla aninhada
d = ((1, 2, 3), (4, 5, 6))
```

### **Principais operações com tuplas:**
| Operação | Descrição | Exemplo |
|----------|----------|---------|
| `len(tupla)` | Retorna o número de elementos na tupla. | `len(tupla)` |
| `tupla[i]` | Acessa um elemento pelo índice. | `tupla[1]` |
| `tupla[i:j]` | Fatiamento da tupla. | `tupla[1:3]` |
| `tupla.index(item)` | Retorna o índice da primeira ocorrência do item. | `tupla.index(20)` |
| `tupla.count(item)` | Conta quantas vezes um item aparece. | `tupla.count(10)` |

### **Exemplo prático com tuplas:**
```python
tupla = (10, 20, 30, 40, 50)
print(tupla[1])      # Acessando o segundo elemento
print(tupla[-1])     # Último elemento da tupla
print(tupla[1:4])    # Fatiamento: (20, 30, 40)
```

### **Conversão entre listas e tuplas**
Para converter uma **lista** em **tupla**:
```python
lista = [1, 2, 3]
tupla = tuple(lista)
```
Para converter uma **tupla** em **lista**:
```python
tupla = (1, 2, 3)
lista = list(tupla)
```

---

## **3. Operações comuns em Listas e Tuplas**
### **Concatenação**
```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2  # Saída: [1, 2, 3, 4, 5, 6]
```
```python
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2  # Saída: (1, 2, 3, 4, 5, 6)
```

### **Repetição**
```python
print([1, 2, 3] * 3)   # Saída: [1, 2, 3, 1, 2, 3, 1, 2, 3]
```
```python
print((1, 2, 3) * 3)   # Saída: (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

### **Percorrendo com `for`**
```python
for item in [1, 2, 3]:
    print(item)
```
```python
for item in (1, 2, 3):
    print(item)
```

### **List Comprehension (Apenas Listas)**
```python
quadrados = [x**2 for x in range(5)]
print(quadrados)  # Saída: [0, 1, 4, 9, 16]
```

---

## **4. Diferenças entre Listas e Tuplas**
| Característica | Lista (`list`) | Tupla (`tuple`) |
|--------------|--------------|--------------|
| Mutabilidade | Mutável | Imutável |
| Desempenho | Mais lenta | Mais rápida |
| Memória | Ocupa mais espaço | Ocupa menos espaço |
| Quando usar? | Dados dinâmicos e mutáveis | Dados fixos e imutáveis |

---

## **Conclusão**
- **Listas** são flexíveis e poderosas, mas podem ser mais pesadas.
- **Tuplas** são rápidas e eficientes, mas não podem ser modificadas.
- Métodos como `append()`, `sort()` e `pop()` são essenciais para listas.
- O conhecimento sobre **fatiamento, indexação e manipulação de dados** é fundamental para ambas.