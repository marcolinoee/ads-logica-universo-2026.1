# caulculo de media de notas

#inserir as notas do aluno


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

#calcular a média das notas

media = (nota1 + nota2 + nota3) / 3

#exibir a média das notas

print(f"A média das notas é: {media:.2f}")

if media >= 7:
    print("Parabéns! Você foi aprovado.")
elif media >= 5:
    print("Você está de recuperação.")
else:
    print("mas ce é burro em!!! reprovado!!!.")