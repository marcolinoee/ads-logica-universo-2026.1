# Entrada de dados
idade = int(input("Digite sua idade: "))
experiencia = int(input("Digite seus anos de experiência: "))

# A lógica booleana armazena o resultado da comparação diretamente na variável
acesso = (idade >= 18) and (experiencia > 2)

# Saída de dados
print(f"Acesso Liberado: {acesso}")