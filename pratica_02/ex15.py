maior = -1

for i in range(5):

    nota = float(input(f"Digite a nota do aluno {i + 1}: "))

    if nota > maior:
        maior = nota

print(f"A maior nota foi: {maior}")

