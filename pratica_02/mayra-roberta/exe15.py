maior = 0

for i in range(5):
    nota = float(input("Digite a nota do aluno: "))
    if nota > maior:
        maior = nota

print("A maior nota foi:", maior)