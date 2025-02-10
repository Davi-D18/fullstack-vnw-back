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

---

## Funções em Python

### Conceito e importância

- **Definição:**  
  Uma função é um bloco de código reutilizável que realiza uma tarefa específica.  
  Ela ajuda a organizar o código, tornando-o modular e mais fácil de manter.

- **Vantagens do uso de funções:**  
  - **Reutilização:** Você pode chamar a mesma função várias vezes sem repetir o código.  
  - **Clareza:** Divide o problema em partes menores e mais compreensíveis.  
  - **Facilidade de teste:** Cada função pode ser testada individualmente.

### Como declarar e usar funções

- **Sintaxe básica:**
  ```python
  def minha_funcao(param1, param2):
      """
      Descrição: Essa função soma dois números.
      """
      resultado = param1 + param2
      return resultado
  ```
  - Para chamar a função:
  ```python
  soma = minha_funcao(3, 4)
  print(soma)  # Saída: 7
  ```

- **Funções sem retorno:**  
  Se não usar `return`, a função retorna `None` por padrão.
  ```python
  def imprimir_mensagem():
      print("Olá, mundo!")
      
  imprimir_mensagem()  # Imprime a mensagem e retorna None
  ```

### Tipos de parâmetros

- **Parâmetros posicionais:**  
  São passados na ordem definida.
  ```python
  def saudacao(nome, idade):
      print(f"Olá, {nome}! Você tem {idade} anos.")

  saudacao("Carlos", 25)
  ```

- **Parâmetros nomeados (keyword arguments):**  
  Permitem especificar os nomes dos parâmetros ao chamar a função.
  ```python
  saudacao(idade=30, nome="Mariana")
  ```

- **Parâmetros com valor padrão:**  
  Caso o argumento não seja fornecido, usa-se o valor padrão definido.
  ```python
  def saudacao(nome, mensagem="Bem-vindo"):
      print(f"{mensagem}, {nome}!")

  saudacao("Rafael")               # Usa o valor padrão "Bem-vindo"
  saudacao("Rafael", "Olá")        # Sobrescreve o valor padrão
  ```

- **Parâmetros arbitrários:**  
  Em Python, às vezes você pode querer escrever uma função que pode aceitar um número variável de argumentos. Para isso, você pode usar `*args` para argumentos posicionais e `**kwargs` para argumentos nomeados.

  - **`*args`:**  
    `*args` permite que você passe um número variável de argumentos posicionais para uma função. Esses argumentos são recebidos como uma tupla.

    **Exemplo:**
    ```python
    def listar_nomes(*nomes):
        for nome in nomes:
            print(nome)

    listar_nomes("Ana", "Carlos", "Beatriz")
    ```
    **Explicação:**
    - A função `listar_nomes` pode receber qualquer quantidade de nomes.
    - Dentro da função, `nomes` é uma tupla contendo todos os argumentos passados.
    - O loop `for` percorre cada nome na tupla e o imprime.

  - **`**kwargs`:**  
    `**kwargs` permite que você passe um número variável de argumentos nomeados (ou seja, argumentos passados como chave-valor) para uma função. Esses argumentos são recebidos como um dicionário.

    **Exemplo:**
    ```python
    def exibir_detalhes(**detalhes):
        for chave, valor in detalhes.items():
            print(f"{chave}: {valor}")

    exibir_detalhes(nome="Ana", idade=30, cidade="São Paulo")
    ```
    **Explicação:**
    - A função `exibir_detalhes` pode receber qualquer quantidade de argumentos nomeados.
    - Dentro da função, `detalhes` é um dicionário contendo todos os argumentos nomeados passados.
    - O loop `for` percorre cada par chave-valor no dicionário e os imprime.

  - **Combinação de `*args` e `**kwargs`:**  
    Você também pode combinar `*args` e `**kwargs` em uma única função para aceitar tanto argumentos posicionais quanto nomeados.

    **Exemplo:**
    ```python
    def combinar_argumentos(*args, **kwargs):
        print("Argumentos posicionais:", args)
        print("Argumentos nomeados:", kwargs)

    combinar_argumentos(1, 2, 3, nome="Ana", idade=30)
    ```
    **Explicação:**
    - A função `combinar_argumentos` pode receber tanto argumentos posicionais quanto nomeados.
    - `args` é uma tupla contendo os argumentos posicionais.
    - `kwargs` é um dicionário contendo os argumentos nomeados.

### Funções anônimas (lambda)

- **Definição:**  
  São funções pequenas, definidas em uma única linha sem um nome explícito.  
  *Uso comum:* em funções de ordem superior, como `map()`, `filter()` e `sorted()`.
  ```python
  quadrado = lambda x: x ** 2
  print(quadrado(5))  # Saída: 25
  ```
  Essa sintaxe reduz a necessidade de criar funções completas para operações simples.  

### Escopo de variáveis

- **Variáveis locais:**  
  Definidas dentro de uma função e acessíveis apenas nela.
  ```python
  def exemplo():
      x = 10  # variável local
      print(x)
  exemplo()
  # print(x)  -> Isso geraria um erro, pois x não é global.
  ```

- **Variáveis globais:**  
  Definidas fora de qualquer função, podem ser acessadas (mas não é recomendável modificá-las diretamente dentro das funções, para evitar efeitos colaterais inesperados).  
