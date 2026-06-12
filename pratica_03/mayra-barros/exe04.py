def calcular_media(n1, n2):
    return (n1 + n2) / 2

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

# Programa principal
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = calcular_media(nota1, nota2)
situacao = verificar_situacao(media)

print(f"A média do aluno é: {media:.1f}")
print(f"Situação: {situacao}")
