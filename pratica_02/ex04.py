senha = ""

while senha != "acesso":
    senha = input("Digite a senha: ")

    if senha != "acesso":
        print("Senha incorreta. Tente novamente.")

print("Acesso liberado!")