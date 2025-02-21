## Inserção de Dados

Para inserir dados em uma tabela, utilize o comando:
```sql
-- Insere um novo registro na tabela 'nome_tabela'
INSERT INTO nome_tabela (nome, idade, email) VALUES ('João', 30, 'joao@example.com');
-- 'INSERT INTO' especifica a tabela e as colunas onde os dados serão inseridos
-- 'VALUES' fornece os valores correspondentes para cada coluna
```

## Seleção de Dados

Para selecionar dados de uma tabela, utilize o comando:
```sql
-- Seleciona todos os registros da tabela 'nome_tabela'
SELECT * FROM nome_tabela;
-- 'SELECT *' seleciona todas as colunas
-- 'FROM' especifica a tabela de onde os dados serão selecionados
```

Para selecionar colunas específicas:
```sql
-- Seleciona apenas as colunas 'nome' e 'email' da tabela 'nome_tabela'
SELECT nome, email FROM nome_tabela;
-- 'SELECT' seguido pelos nomes das colunas especifica quais colunas serão retornadas
```

## Atualização de Dados

Para atualizar dados em uma tabela, utilize o comando:
```sql
-- Atualiza a idade para 31 onde o nome é 'João' na tabela 'nome_tabela'
UPDATE nome_tabela SET idade = 31 WHERE nome = 'João';
-- 'UPDATE' especifica a tabela a ser atualizada
-- 'SET' define as novas valores para as colunas especificadas
-- 'WHERE' filtra os registros que serão atualizados
```

## Exclusão de Dados

Para excluir dados de uma tabela, utilize o comando:
```sql
-- Exclui o registro onde o nome é 'João' da tabela 'nome_tabela'
DELETE FROM nome_tabela WHERE nome = 'João';
-- 'DELETE FROM' especifica a tabela de onde os dados serão excluídos
-- 'WHERE' filtra os registros que serão excluídos
```

## Exclusão de Tabela

Para excluir uma tabela, utilize o comando:
```sql
-- Exclui a tabela 'nome_tabela' do banco de dados
DROP TABLE nome_tabela;
-- 'DROP TABLE' exclui a tabela e todos os seus dados
```

## Exclusão de Banco de Dados

Para excluir um banco de dados, utilize o comando:
```sql
-- Exclui o banco de dados 'nome_banco'
DROP DATABASE nome_banco;
-- 'DROP DATABASE' exclui o banco de dados e todos os seus objetos
```
