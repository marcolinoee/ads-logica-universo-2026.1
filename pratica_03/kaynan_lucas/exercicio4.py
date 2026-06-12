def calcular_media(n1, n2):
    return (n1 + n2) / 2

def verificar_situacao(media):
     if media >= 7:
        return "Aprovado"
     else:
        return "Reprovado"
     
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

media = calcular_media(nota1, nota2)
situacao = verificar_situacao(media)

print(f"A média das notas é: {media}")
print(f"Situação: {situacao}")