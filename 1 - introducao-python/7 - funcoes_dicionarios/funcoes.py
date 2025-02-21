nome = input("Digite seu nome: ")
senha = int(input("Digite sua senha: "))

def login(nome, senha):
    if nome == "admin" and senha == 123:
        return "Bem-vindo admin!"
    else:
        return "Usuário ou senha inválidos!"
    

resultado = login(nome, senha)
print(resultado)
    