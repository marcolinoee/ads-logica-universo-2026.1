qtd_alunos = int(input("Quantos alunos há na turma? "))

aprovados = 0
recuperacao = 0
reprovados = 0

for i in range(qtd_alunos):
    media = float(input("Digite a média do aluno: "))

    if media >= 7:
        aprovados = aprovados + 1

    elif media >= 4:
        recuperacao = recuperacao + 1

    else:
        reprovados = reprovados + 1

print(f"Alunos aprovados: {aprovados}")
print(f"Alunos em recuperação: {recuperacao}")
print(f"Alunos reprovados: {reprovados}")