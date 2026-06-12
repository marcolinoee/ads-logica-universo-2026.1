quantidade = int(input("Quantidade de alunos: "))

aprovados = 0
recuperacao = 0
reprovados = 0

for i in range(quantidade):
    media = float(input("Digite a média do aluno: "))

    if media >= 7:
        aprovados += 1
    elif media >= 5:
        recuperacao += 1
    else:
        reprovados += 1

print("Aprovados:", aprovados)
print("Recuperação:", recuperacao)
print("Reprovados:", reprovados)