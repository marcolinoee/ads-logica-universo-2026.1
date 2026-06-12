# ex18.py
# Aula com mais faltas

maior_qtd_faltas = 0
aula_com_mais_faltas = 0 

presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

for coluna in range(len(presencas[0])):
    total_faltas = 0 

    for linha in range(len(presencas)):
        if presencas[linha][coluna] == "F":
            total_faltas += 1

        if total_faltas > maior_qtd_faltas:
            maior_qtd_faltas = total_faltas
            aula_com_mais_faltas = coluna

print("Aula com mais faltas:", aula_com_mais_faltas)
print("Quantidade de faltas:", maior_qtd_faltas)
