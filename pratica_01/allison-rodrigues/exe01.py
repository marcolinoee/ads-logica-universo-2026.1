# Pega os dados do usuário
nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))  # int() porque vai fazer conta
altura = float(input("Digite sua altura em metros: "))        # float() porque tem vírgula

# Calcula a idade
ano_atual = 2026  # estamos em 2026
idade = ano_atual - ano_nascimento

# Mostra o resultado
print("Olá,", nome + "! Você tem", idade, "anos e sua altura é de", altura, "m. Registro concluído.")