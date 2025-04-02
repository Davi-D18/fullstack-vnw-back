from flask import json

from ..repository.repository import criar_tabela, inserir_dados


def inserir_informacoes(titulo, categoria, autor, image_url):
  tabela_existe = criar_tabela()
  
  if not tabela_existe:
    return json.dumps({"message": "Erro ao criar a tabela"}), 500

  dados_inseridos = inserir_dados(titulo, categoria, autor, image_url)

  if not dados_inseridos:
    return json.dumps({"message": "Erro ao inserir dados"}), 500

  return json.dumps({"message": "Dados inseridos com sucesso"}), 201