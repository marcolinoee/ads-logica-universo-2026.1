def calcular_media(n1, n2):
    return (n1 + n2) / 2

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

n1=10
n2=5

media = calcular_media(n1, n2)

resultado = verificar_situacao(media)

print(resultado)
