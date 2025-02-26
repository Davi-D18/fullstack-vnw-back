### Inserindo Dados com INSERT INTO

O comando **INSERT INTO** adiciona uma nova linha (registro) na tabela. A estrutura básica é:

```sql
INSERT INTO nome_da_tabela (coluna1, coluna2, coluna3)
VALUES (valor1, valor2, valor3);
```

**Exemplo:**

```sql
INSERT INTO usuarios (nome, idade)
VALUES ('Maria', 28);
```

Esse comando cria um novo registro na tabela `usuarios` com o nome "Maria" e a idade 28.

### Modificando Dados com UPDATE

Depois de inserir os dados, se precisar alterar alguma informação de um registro já existente, use o comando **UPDATE**. A estrutura básica é:

```sql
UPDATE nome_da_tabela
SET coluna = novo_valor
WHERE condição;
```

**Exemplo:**

```sql
UPDATE usuarios
SET idade = 29
WHERE nome = 'Maria';
```

A cláusula `WHERE` é importante para garantir que apenas o(s) registro(s) desejado(s) sejam modificados. Sem ela, todas as linhas da tabela seriam atualizadas.

### Alterando a Estrutura de uma Coluna (Definição da Tabela)

Se o que você deseja é **modificar a definição** de uma coluna (por exemplo, alterar o tipo de dado ou o tamanho da coluna), você deve usar o comando **ALTER TABLE**.

**Exemplo:**  
Para alterar a coluna `nome` de `CHAR(30)` para `VARCHAR(50)`:

```sql
ALTER TABLE usuarios
MODIFY COLUMN nome VARCHAR(50);
```

**Explicação:**  
- **ALTER TABLE usuarios**: indica a tabela que terá sua estrutura modificada.  
- **MODIFY COLUMN nome VARCHAR(50)**: altera a definição da coluna `nome` para o tipo `VARCHAR` com tamanho 50.

---

Ambos os comandos são fundamentais para gerenciar dados e estruturas em SQL, mas servem para propósitos diferentes:  
- **UPDATE** modifica os dados (o conteúdo das colunas).  
- **ALTER TABLE** modifica a estrutura (o formato ou definição das colunas).

### DELETE: Sintaxe Básica

```sql
DELETE FROM nome_da_tabela
WHERE condição;
```

- **DELETE FROM nome_da_tabela:** Indica de qual tabela os registros serão removidos.
- **WHERE condição:** Especifica quais registros devem ser excluídos. **Atenção:** Se omitir a cláusula `WHERE`, **todos os registros** da tabela serão deletados.

---

### Exemplo Prático

Imagine que você tem a tabela `usuarios` e deseja remover o registro do usuário chamado "Maria". Você pode fazer o seguinte:

```sql
DELETE FROM usuarios
WHERE nome = 'Maria';
```

Esse comando remove apenas os registros onde a coluna `nome` é igual a "Maria".

### Dicas Importantes

- **Uso do WHERE:** Sempre utilize a cláusula `WHERE` para evitar excluir todos os registros acidentalmente.
- **Backup:** Se estiver trabalhando em um ambiente de produção, considere fazer um backup ou testar a query em um ambiente de desenvolvimento antes de executar a exclusão.

Dessa forma, o comando **DELETE** permite controlar quais dados serão removidos do seu banco de dados de forma segura e precisa.