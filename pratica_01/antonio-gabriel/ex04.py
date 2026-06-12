idade = int(input("Qual a sua idade? "))
experiencia = float(input("Digite quantos de experiência você tem na área: "))

acesso = idade >= 18 and experiencia >= 2
print ("Acesso liberado:", acesso)