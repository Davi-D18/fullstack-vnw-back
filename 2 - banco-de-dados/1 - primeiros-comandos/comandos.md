# Comandos SQL Básicos

## Criação de Banco de Dados

Para criar um banco de dados, utilize o comando:
```sql
CREATE DATABASE nome_banco;
```

Alguns comandos:

Seleciona o banco de dados
```sql
USE nome_banco;
```

Cria uma tabela
```sql
CREATE TABLE nome_tabela(
  nome_coluna tipo_dado(caracteres) / outras_informacoes,
  id INT AUTO_INCREMENT PRIMARY KEY 
  nome VARCHAR(50),
)

CREATE TABLE nome_tabela (
  id INT AUTO_INCREMENT PRIMARY KEY, -- Coluna de ID com auto incremento e chave primária
  nome VARCHAR(50) NOT NULL,         -- Coluna de nome com tipo VARCHAR e máximo de 50 caracteres
  idade INT,                         -- Coluna de idade com tipo INT
  email VARCHAR(100) UNIQUE          -- Coluna de email com tipo VARCHAR e máximo de 100 caracteres, valor único
);
```
## Criação de Banco de Dados

Para criar um banco de dados, utilize o comando:
```sql
CREATE DATABASE nome_banco;
```

## Seleção de Banco de Dados

Para selecionar um banco de dados para uso, utilize o comando:
```sql
USE nome_banco;
```

## Criação de Tabela

Para criar uma tabela, utilize o comando:
```sql
CREATE TABLE nome_tabela (
  id INT AUTO_INCREMENT PRIMARY KEY, -- Coluna de ID com auto incremento e chave primária
  nome VARCHAR(50) NOT NULL,         -- Coluna de nome com tipo VARCHAR e máximo de 50 caracteres
  idade INT,                         -- Coluna de idade com tipo INT
  email VARCHAR(100) UNIQUE          -- Coluna de email com tipo VARCHAR e máximo de 100 caracteres, valor único
);
```
