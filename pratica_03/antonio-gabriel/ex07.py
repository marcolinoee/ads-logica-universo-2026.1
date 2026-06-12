# Refatorando codigo monolitico

# Código original abaixo:
n1 = 8
n2 = 6
media = (n1 + n2) / 2

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

# Meu código abaixo:

n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))

def calcular_media(n1, n2):
    return (n1 + n2) / 2

def verificar_situacao(media):
    if media >=7:
        return "Aprovado"
    else:
        return "Reprovado"
    
print(verificar_situacao(media))