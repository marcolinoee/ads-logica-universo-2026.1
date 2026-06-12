qtd_alunos = int(input("Digite a quantidade de alunos: "))

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

print("Aprovados:", aprovados)
print("Recuperação:", recuperacao)
print("Reprovados:", reprovados)