maior_nota = 0

for i in range(5):
    nota = float(input("Digite uma nota: "))
    if nota > maior_nota:
        maior_nota = nota

print("A maior nota é:", maior_nota)

# O 'while' funcionaria, mas o 'for' é melhor por ser uma quantidade fixa de vezes (5).
# O 'while' faria sentido se o programa rodasse até o usuário digitar uma nota negativa para parar.