idade = int(input("Digite a sua idade: "))

if idade > 59:
    print("Você é idoso! :) ")
elif idade > 17:
    print("Você é maior de idade! :) ")
elif idade < 0:
    print("Você não inseriu uma idade válida! :( ")
else:
    print("Você é menor de idade! :) ")