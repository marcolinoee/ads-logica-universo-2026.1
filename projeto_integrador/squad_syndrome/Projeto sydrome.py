def cadastrar_barras():
    barras = []

    qtd_barras = int(input("Quantas barras deseja cadastrar? "))

    for i in range(qtd_barras):
        nome = input("Nome da barra: ")
        barras.append(nome)

    return barras


def cadastrar_linhas(barras):
    linhas = []

    qtd_linhas = int(input("Quantas ligações deseja criar? "))

    for i in range(qtd_linhas):
        origem = input("Barra origem: ")
        destino = input("Barra destino: ")

        if origem in barras and destino in barras:

            resistencia = float(input("Resistência da linha: "))

            linhas.append([origem, destino, resistencia])

        else:
            print("Barra inválida!")

    return linhas


def iniciar_tensoes(barras):
    tensoes = {}

    for barra in barras:
        tensoes[barra] = 100.0

    return tensoes


def calcular_tensoes(barras, linhas, tensoes):

    # Correntes fixas do teste
    correntes = {
        barras[1]: -10.0,
        barras[2]: -5.0
    }

    erro = 1
    iteracao = 1

    while erro > 0.001:

        erro = 0

        for barra in barras[1:]:

            valor_antigo = tensoes[barra]

            numerador = correntes[barra]
            denominador = 0

            for linha in linhas:

                origem = linha[0]
                destino = linha[1]
                resistencia = linha[2]

                if origem == barra:
                    numerador += tensoes[destino] / resistencia
                    denominador += 1 / resistencia

                elif destino == barra:
                    numerador += tensoes[origem] / resistencia
                    denominador += 1 / resistencia

            novo_valor = numerador / denominador

            tensoes[barra] = novo_valor

            diferenca = abs(novo_valor - valor_antigo)

            if diferenca > erro:
                erro = diferenca

        print("Iteração", iteracao, tensoes)

        iteracao += 1

    return tensoes

# =====================================
# ALUNO 3 - ARQUITETO DE GRAFOS POO
# =====================================

class Barra:

    def __init__(self, nome):
        self.nome = nome
        self.tensao = 100.0

    def __repr__(self):
        return f"Barra({self.nome}, {self.tensao}V)"


class Linha:

    def __init__(self, origem, destino, resistencia):
        self.origem = origem
        self.destino = destino
        self.resistencia = resistencia

    def __repr__(self):
        return f"Linha({self.origem}->{self.destino}, R={self.resistencia})"


def criar_objetos_poo(barras, linhas, tensoes):

    lista_barras = []

    for nome in barras:
        barra = Barra(nome)
        barra.tensao = tensoes[nome]
        lista_barras.append(barra)

    lista_linhas = []

    for origem, destino, resistencia in linhas:
        lista_linhas.append(
            Linha(origem, destino, resistencia)
        )

    return lista_barras, lista_linhas


# =====================================
# ALUNO 4 - ANALISTA DE PERDAS
# =====================================

VERMELHO = "\033[91m"
RESET = "\033[0m"


def gerar_relatorio(tensoes, linhas):

    print("\n===== RELATÓRIO FINAL =====")

    print("\nTENSÕES DAS BARRAS")

    for barra, tensao in tensoes.items():

        if tensao < 93:

            print(
                f"{VERMELHO}{barra}: "
                f"{tensao:.2f} V [SUBTENSÃO]{RESET}"
            )

        else:

            print(
                f"{barra}: {tensao:.2f} V"
            )

    print("\nPERDAS NAS LINHAS")

    perda_total = 0

    for origem, destino, resistencia in linhas:

        corrente = abs(
            (tensoes[origem] - tensoes[destino])
            / resistencia
        )

        perda = (corrente ** 2) * resistencia

        perda_total += perda

        print(
            f"{origem} -> {destino} | "
            f"Perda = {perda:.2f} W"
        )

    print(
        f"\nPerda total da rede: "
        f"{perda_total:.2f} W"
    )



def main():

    barras = cadastrar_barras()

    linhas = cadastrar_linhas(barras)

    tensoes = iniciar_tensoes(barras)

    resultado = calcular_tensoes(barras, linhas, tensoes)

    lista_barras, lista_linhas = criar_objetos_poo(
      barras,
      linhas,
      resultado
    )

    print("\nConvergiu!")
    print("Resultado final:")
    print(resultado)

    gerar_relatorio(resultado, linhas)


main()