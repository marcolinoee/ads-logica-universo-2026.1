# ESTADO INICIAL
populacao = 1000
agua = 5000
energia = 3000
dinheiro = 10000
poluicao = 10

ano = 1

def linha():
    print("=" * 40)

def mostrar_status():
    linha()
    print(f"ANO {ano}")
    linha()
    print(f"População : {populacao}")
    print(f"Água      : {agua}")
    print(f"Energia   : {energia}")
    print(f"Dinheiro  : {dinheiro}")
    print(f"Poluição  : {poluicao}")
    linha()

def grafico(valor, escala):
    barras = max(0, valor // escala)
    return "*" * barras

while ano <= 15:

    mostrar_status()

    print("\nAções:")
    print("1 - Construir usina (-2000)")
    print("2 - Tratar água (-1000)")
    print("3 - Sustentabilidade (-1500)")
    print("4 - Passar turno")

    escolha = input("Opção: ")

    # AÇÕES
    if escolha == "1":
        if dinheiro >= 2000:
            energia += 1200
            poluicao += 6
            dinheiro -= 2000
            print("Usina construída.")
        else:
            print("Dinheiro insuficiente.")

    elif escolha == "2":
        if dinheiro >= 1000:
            agua += 1200
            poluicao -= 4
            dinheiro -= 1000
            print("Água tratada.")
        else:
            print("Dinheiro insuficiente.")

    elif escolha == "3":
        if dinheiro >= 1500:
            poluicao -= 8
            dinheiro -= 1500
            print("Projeto sustentável aplicado.")
        else:
            print("Dinheiro insuficiente.")

    # PRODUÇÃO AUTOMÁTICA
    agua += 300
    energia += 200

    # CRESCIMENTO
    if agua > 1000 and energia > 1000:
        crescimento = int(populacao * 0.05)
    else:
        crescimento = int(populacao * 0.01)

    populacao += crescimento

    # CONSUMO
    consumo_agua = populacao // 2
    consumo_energia = populacao // 3

    agua -= consumo_agua
    energia -= consumo_energia

    # ECONOMIA
    dinheiro += populacao // 3
    dinheiro -= poluicao

    # POLUIÇÃO
    poluicao += 2

    # EVENTOS (SEM RANDOM)
    if ano % 5 == 0:
        print(" Seca! Água diminuiu.")
        agua -= 800

    elif ano % 3 == 0:
        print(" Investimento externo!")
        dinheiro += 2000

    elif ano % 2 == 0:
        print(" Movimento ecológico!")
        poluicao -= 5

    # LIMITES
    agua = max(0, agua)
    energia = max(0, energia)
    poluicao = max(0, poluicao)

    # CONSEQUÊNCIAS
    if agua == 0 or energia == 0:
        perda = int(populacao * 0.05)
        populacao -= perda
        print("Falta de recursos. População reduziu.")

    if poluicao > 120:
        perda = int(populacao * 0.03)
        populacao -= perda
        print("Poluição crítica. População reduzida.")

    populacao = max(0, populacao)

    # GRÁFICOS
    print("\nGráficos:")
    print("População :", grafico(populacao, 100))
    print("Poluição  :", grafico(poluicao, 2))
    print("Água      :", grafico(agua, 200))
    print("Energia   :", grafico(energia, 200))

    if populacao == 0:
        print("\n A cidade colapsou.")
        break

    ano += 1

print("\n Simulação finalizada.")