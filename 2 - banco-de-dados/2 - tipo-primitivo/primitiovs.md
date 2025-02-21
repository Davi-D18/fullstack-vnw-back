Tipos primitivos -> Tipos de dados em Banco de dados
- "Pensar no futuro"

| Tipo           | Descrição                                      | Exemplo                         |
|--------------|--------------------------------|-------------------------------|
| **INT / INTEGER** | Inteiros (-2B a 2B)                          | 2000000000                     |
| **BIGINT**       | Números grandes (-9 quintilhões a +9 quintilhões) | 9000000000000000000            |
| **DECIMAL**      | Números decimais precisos                      | 10.50, -3.75                   |
| **CHAR(n)**      | Texto fixo (1 a 255 caracteres)                | CHAR(10) → 'Hello'             |
| **VARCHAR(n)**   | Texto variável (1 a 65.535 caracteres)         | VARCHAR(20) → 'Hello'          |
| **DATE / DATETIME** | Data / Data e hora                          | 2024-02-16 / 2024-02-16 14:30:00 |

Alguns comandos úteis:
| Descrição                                         | Comando SQL                           |
|--------------------------------------------------|---------------------------------------|
| Comando para criar um Banco de Dados            | `CREATE DATABASE nome_do_banco;`      |
| Comando para usar um Banco de Dados             | `USE nome_do_banco;`                  |
| Comando para criar uma tabela                   | `CREATE TABLE nome_da_tabela(colunas);` |
| Exibir tabelas do Banco de Dados                | `SHOW TABLES;`                        |
| Exibir estrutura de uma tabela                  | `DESC nome_tabela;`                   |
| *Excluir uma tabela*                             | `DROP TABLE nome_tabela;`             |
| Excluir um Banco de Dados                       | `DROP DATABASE nome_do_banco;`        |
| Deletar dados de uma tabela (permanente)        | `TRUNCATE TABLE nome_tabela;`         |
| Exibir informações de uma tabela | `DESC nome_tabela` |

## Constrains
"Constraints" (ou restrições) são regras aplicadas às colunas de uma tabela para garantir a integridade e a precisão dos dados. Elas ajudam a manter a consistência dos dados e a prevenir erros.

| Tipos de Constraints              | Como podemos utilizar                                      |
|-----------------------------------|----------------------------------------------------------|
| **Primary Key (Chave Primária)**  | Identifica os dados através de valores únicos.          |
| **AUTO_INCREMENT**                | Gera valores numéricos automaticamente.                 |
| **NOT NULL**                      | Impede que sejam colocados valores nulos em uma coluna. |

### Exemplo de uso:
```sql
id INT AUTO_INCREMENT PRIMARY KEY  
nome VARCHAR(30) NOT NULL  
```
