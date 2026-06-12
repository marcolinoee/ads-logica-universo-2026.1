# Solicita os dados do usuário
nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))
altura = float(input("Digite sua altura em metros: "))

# Define o ano atual
ano_atual = 2026

# Calcula a idade
idade = ano_atual - ano_nascimento

# Exibe a mensagem final
print(f"Olá, {nome}! Você tem {idade} anos e sua altura é de {altura}m. Registro concluído.")