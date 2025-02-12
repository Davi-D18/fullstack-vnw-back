## Tuplas em Python

### O que são e por que usá-las

- **Definição:**  
  Uma tupla é uma coleção ordenada de elementos que, depois de criada, **não pode ser alterada** (imutável).  
  Isso garante que os dados armazenados permaneçam inalterados durante a execução do programa.  
  *Exemplo:* Usar tuplas para armazenar coordenadas fixas, dias da semana ou dados de configuração que não devem mudar.

- **Vantagens:**  
  - **Segurança:** Garante que os dados não sejam modificados acidentalmente.  
  - **Desempenho:** Em geral, operações com tuplas são mais rápidas que com listas por conta da imutabilidade.  
  - **Uso como chave em dicionários:** Por serem imutáveis, podem ser usadas como chaves (o que não é possível com listas).

### Como criar e acessar tuplas

- **Criação Simples:**  
  Você pode criar uma tupla colocando os elementos entre parênteses e separados por vírgulas.  
  ```python
  minha_tupla = (1, "Python", 3.14)
  ```
  *Dica:* Para criar uma tupla com **um único elemento**, não se esqueça da vírgula:
  ```python
  tupla_um = (42,)
  ```

- **Acesso aos Elementos:**  
  A indexação funciona como nas listas (o primeiro elemento tem índice 0).  
  ```python
  print(minha_tupla[0])   # Saída: 1
  print(minha_tupla[-1])  # Saída: 3.14
  ```

### Operações e métodos úteis

- **Fatiamento (Slicing):**  
  Você pode extrair partes da tupla:
  ```python
  sub_tupla = minha_tupla[1:3]  # Retorna ("Python", 3.14)
  ```

- **Métodos principais:**  
  - **count():** Conta quantas vezes um elemento aparece.
    ```python
    numeros = (1, 2, 3, 2, 4)
    print(numeros.count(2))  # Saída: 2
    ```
  - **index():** Retorna o índice da primeira ocorrência de um elemento.
    ```python
    print(numeros.index(3))  # Saída: 2
    ```

- **Desempacotamento:**  
  Você pode “desempacotar” os valores de uma tupla em variáveis separadas.
  ```python
  coordenada = (10, 20)
  x, y = coordenada
  print(x)  # Saída: 10
  print(y)  # Saída: 20
  ```

- **Tuplas como retorno de funções:**  
  Funções podem retornar múltiplos valores agrupados em uma tupla:
  ```python
  def min_max(valores):
      return min(valores), max(valores)

  minimo, maximo = min_max([4, 7, 1, 9])
  print(minimo)  # Saída: 1
  print(maximo)  # Saída: 9
  ```

- **Tuplas nomeadas (namedtuple):**  
  Se desejar dar nomes aos elementos para aumentar a clareza, use `namedtuple` da biblioteca `collections`:
  ```python
  from collections import namedtuple
  Pessoa = namedtuple('Pessoa', ['nome', 'idade'])
  p = Pessoa(nome="Ana", idade=30)
  print(p.nome)   # Saída: Ana
  print(p.idade)  # Saída: 30
  ```
  Essas ferramentas deixam o código mais legível e ajudam a identificar melhor o significado dos dados armazenados.  
  citeturn0search0

### Comparação com listas

- **Listas:**  
  São mutáveis (você pode alterar, adicionar ou remover elementos). São ideais quando a coleção de dados pode mudar durante a execução.
  
- **Tuplas:**  
  São imutáveis, o que oferece maior segurança para dados constantes e pode melhorar o desempenho.  