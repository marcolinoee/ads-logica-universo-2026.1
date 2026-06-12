#Sim, daria pra usar while também.
#Ele seria melhor caso a gente não soubesse quantas notas seriam digitadas, porque o programa poderia continuar rodando até o usuário decidir parar.



maior = 0

for i in range(5):
    nota = float(input("Digite uma nota: "))

    if nota > maior:
        maior = nota

print("Maior nota:", maior)