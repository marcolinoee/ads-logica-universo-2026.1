# ESTADO INICIAL
populacao = 1000
agua = 5000
energia = 3000
dinheiro = 10000
poluicao = 10

ano = 1

def linha():
    print("=" * 40)

# [FIX 5] Parâmetros explícitos — sem dependência de variáveis globais
def mostrar_status(ano, populacao, agua, energia, dinheiro, poluicao):
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
    barras = min(50, max(0, valor // escala))
    return "*" * barras

while ano <= 15:

    mostrar_status(ano, populacao, agua, energia, dinheiro, poluicao)

    print("\nAções:")
    print("1 - Construir usina (-2000)")
    print("2 - Tratar água (-1000)")
    print("3 - Sustentabilidade (-1500)")
    print("4 - Passar turno")

    # VALIDAÇÃO DA ENTRADA
    while True:
        escolha = input("Opção: ")
        if escolha in ["1", "2", "3", "4"]:
            break
        print("Opção inválida! Digite apenas 1, 2, 3 ou 4.")

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

    elif escolha == "4":
        print("Turno encerrado.")

    # PRODUÇÃO AUTOMÁTICA
    agua += 300
    energia += 200

    # CONSUMO
    consumo_agua = populacao // 2
    consumo_energia = populacao // 3

    agua = max(0, agua - consumo_agua)
    energia = max(0, energia - consumo_energia)

    # [FIX 1] Crescimento calculado APÓS o consumo real
    # Assim a condição reflete os recursos disponíveis de verdade
    if agua > 1000 and energia > 1000:
        crescimento = int(populacao * 0.05)
    else:
        crescimento = int(populacao * 0.01)

    # [FIX 3] Guardar população base ANTES do crescimento
    # para usar na penalidade de falta de recursos
    populacao_antes = populacao
    populacao += crescimento

    # ECONOMIA
    dinheiro += populacao // 3
    dinheiro -= poluicao

    # POLUIÇÃO
    poluicao += 2

    # EVENTOS
    if ano % 5 == 0:
        print("Seca! Água diminuiu.")
        agua -= 800
        agua = max(0, agua)  # [FIX 2] Proteção imediata após evento

    if ano % 3 == 0:
        print("Investimento externo!")
        dinheiro += 2000

    if ano % 2 == 0:
        print("Movimento ecológico!")
        poluicao -= 5
        poluicao = max(0, poluicao)  # [FIX 4] Proteção imediata após evento

    # LIMITES GERAIS
    agua = max(0, agua)
    energia = max(0, energia)
    poluicao = max(0, poluicao)
    dinheiro = max(0, dinheiro)

    # CONSEQUÊNCIAS
    # [FIX 3] Penalidade usa populacao_antes (base real, pré-crescimento)
    if agua == 0 or energia == 0:
        perda = int(populacao_antes * 0.05)
        populacao -= perda
        print("Falta de recursos. População reduziu.")

    if poluicao > 120:
        perda = int(populacao_antes * 0.03)
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
        print("\nA cidade colapsou.")
        break

    ano += 1

print("\nSimulação finalizada.")