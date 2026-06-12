def calcular_media(n1, n2,):
    return (n1 + n2) / 2

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

media = calcular_media(nota1, nota2)
print(f"A média das notas é: {media}")