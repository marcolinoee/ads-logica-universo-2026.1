# Entrada de dados
nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))
altura = float(input("Digite sua altura (em metros): "))

# Defina manualmente o ano atual
ano_atual = 2026

# Cálculo da idade
idade = ano_atual - ano_nascimento

# Saída
print("Olá,", nome + "!", "Você tem", idade, "anos e sua altura é de", altura, "m. Registro concluído.")