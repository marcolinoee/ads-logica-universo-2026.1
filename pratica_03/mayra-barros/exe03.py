def calcular_media(n1, n2):
    return (n1 + n2) / 2

# Programa principal
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = calcular_media(nota1, nota2)

# Exibindo a média com uma casa decimal
print(f"A média do aluno é: {media:.1f}")
