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

  ## Dicionários em Python

  ### Conceito e importância

  - **Definição:**  
    Um dicionário é uma coleção de pares chave-valor, onde cada chave é única e está associada a um valor.  
    Eles são úteis para armazenar dados que precisam ser rapidamente recuperados através de uma chave.

  - **Vantagens do uso de dicionários:**  
    - **Acesso rápido:** Recuperação de valores através de chaves é muito eficiente.
    - **Flexibilidade:** Suporta diferentes tipos de dados como chaves e valores.
    - **Organização:** Permite organizar dados de forma clara e lógica.

  ### Como criar e usar dicionários

  - **Sintaxe básica:**
    ```python
    meu_dicionario = {
        "nome": "João",
        "idade": 25,
        "cidade": "São Paulo"
    }
    ```
    - Para acessar um valor:
    ```python
    nome = meu_dicionario["nome"]
    print(nome)  # Saída: João
    ```

  - **Adicionar ou modificar valores:**  
    Você pode adicionar novos pares chave-valor ou modificar valores existentes.
    ```python
    meu_dicionario["profissao"] = "Engenheiro"
    meu_dicionario["idade"] = 26
    ```

  - **Remover itens:**  
    Use a palavra-chave `del` ou o método `pop()`.
    ```python
    del meu_dicionario["cidade"]
    idade = meu_dicionario.pop("idade")
    ```

  ### Métodos comuns de dicionários

  - **`keys()`:**  
    Retorna uma visão das chaves no dicionário.
    ```python
    chaves = meu_dicionario.keys()
    print(chaves)  # Saída: dict_keys(['nome', 'profissao'])
    ```

  - **`values()`:**  
    Retorna uma visão dos valores no dicionário.
    ```python
    valores = meu_dicionario.values()
    print(valores)  # Saída: dict_values(['João', 'Engenheiro'])
    ```

  - **`items()`:**  
    Retorna uma visão dos pares chave-valor no dicionário.
    ```python
    itens = meu_dicionario.items()
    print(itens)  # Saída: dict_items([('nome', 'João'), ('profissao', 'Engenheiro')])
    ```

  - **`get()`:**  
    Retorna o valor para uma chave, ou um valor padrão se a chave não existir.
    ```python
    idade = meu_dicionario.get("idade", "Não especificado")
    print(idade)  # Saída: Não especificado
    ```

  - **`update()`:**  
    Atualiza o dicionário com pares chave-valor de outro dicionário ou de um iterável de pares chave-valor.
    ```python
    atualizacoes = {"idade": 26, "cidade": "Rio de Janeiro"}
    meu_dicionario.update(atualizacoes)
    ```

  - **`clear()`:**  
    Remove todos os itens do dicionário.
    ```python
    meu_dicionario.clear()
    ```

  ### Iterando sobre dicionários

  - **Iterar sobre chaves:**
    ```python
    for chave in meu_dicionario:
        print(chave)
    ```

  - **Iterar sobre valores:**
    ```python
    for valor in meu_dicionario.values():
        print(valor)
    ```

  - **Iterar sobre pares chave-valor:**
    ```python
    for chave, valor in meu_dicionario.items():
        print(f"{chave}: {valor}")
    ```