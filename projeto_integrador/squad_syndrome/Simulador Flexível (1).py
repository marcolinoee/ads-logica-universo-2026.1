class Barra:
    def __init__(self, nome, tensao):
        self.nome = nome
        self.tensao = tensao

    def __str__(self):
        return f"{self.nome} ({self.tensao}V)"


class Linha:
    def __init__(self, origem, destino, resistencia):
        self.origem = origem
        self.destino = destino
        self.resistencia = resistencia

    def calcular_perda(self):
        # Fórmula simplificada:
        # perda = diferença de tensão × resistência
        diferenca = abs(self.origem.tensao - self.destino.tensao)
        perda = diferenca * self.resistencia
        return perda

    def __str__(self):
        perda = self.calcular_perda()
        return (f"{self.origem.nome} -> {self.destino.nome} | "
                f"Resistência: {self.resistencia}Ω | "
                f"Perda: {perda:.2f}")


class Sistema:
    def __init__(self):
        self.barras = []
        self.linhas = []

    # -----------------------------
    # CADASTRAR BARRAS
    # -----------------------------
    def adicionar_barra(self):
        nome = input("Nome da barra: ")

        while True:
            try:
                tensao = float(input("Tensão da barra (V): "))
                break
            except ValueError:
                print("Digite um valor numérico válido.")

        barra = Barra(nome, tensao)
        self.barras.append(barra)

        print("Barra cadastrada com sucesso!\n")

    # -----------------------------
    # LISTAR BARRAS
    # -----------------------------
    def listar_barras(self):
        if not self.barras:
            print("Nenhuma barra cadastrada.\n")
            return

        print("\nBARRAS CADASTRADAS")
        for i, barra in enumerate(self.barras):
            print(f"{i} - {barra}")

        print()

    # -----------------------------
    # CRIAR LINHAS
    # -----------------------------
    def adicionar_linha(self):
        if len(self.barras) < 2:
            print("Cadastre pelo menos 2 barras.\n")
            return

        self.listar_barras()

        try:
            origem = int(input("Índice da barra de origem: "))
            destino = int(input("Índice da barra de destino: "))

            if origem == destino:
                print("Uma barra não pode ligar nela mesma.\n")
                return

            resistencia = float(input("Resistência do fio (Ω): "))

            linha = Linha(
                self.barras[origem],
                self.barras[destino],
                resistencia
            )

            self.linhas.append(linha)

            print("Ligação criada com sucesso!\n")

        except (ValueError, IndexError):
            print("Entrada inválida.\n")

    # -----------------------------
    # VALIDAR GRAFO
    # -----------------------------
    def validar_grafo(self):
        if not self.barras:
            print("Nenhuma barra cadastrada.\n")
            return

        conectadas = set()

        for linha in self.linhas:
            conectadas.add(linha.origem.nome)
            conectadas.add(linha.destino.nome)

        isoladas = []

        for barra in self.barras:
            if barra.nome not in conectadas:
                isoladas.append(barra.nome)

        print("\nVALIDAÇÃO DO GRAFO")

        if not isoladas:
            print("Todas as barras estão conectadas!\n")
        else:
            print("Barras isoladas:")
            for nome in isoladas:
                print("-", nome)
            print()

    # -----------------------------
    # RELATÓRIO DE PERDAS
    # -----------------------------
    def relatorio(self):
        if not self.linhas:
            print("Nenhuma linha cadastrada.\n")
            return

        print("\nRELATÓRIO DE PERDAS")

        perda_total = 0

        for linha in self.linhas:
            perda = linha.calcular_perda()
            perda_total += perda

            print(linha)

        print(f"\nPerda total da rede: {perda_total:.2f}\n")

    # -----------------------------
    # SIMULAÇÃO ITERATIVA
    # EXEMPLO usando abs() para
    # evitar loop infinito
    # -----------------------------
    def simular_estabilidade(self):
        erro = 10
        iteracao = 0

        print("\nIniciando simulação...\n")

        while abs(erro) > 0.01:
            erro = erro / -2

            print(f"Iteração {iteracao} -> erro = {erro:.4f}")

            iteracao += 1

        print("\nSistema estabilizado!\n")


# ==========================================
# MENU PRINCIPAL
# ==========================================

sistema = Sistema()

while True:
    print("======== MENU ========")
    print("1 - Adicionar barra")
    print("2 - Listar barras")
    print("3 - Criar ligação")
    print("4 - Validar grafo")
    print("5 - Relatório de perdas")
    print("6 - Simular estabilidade")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        sistema.adicionar_barra()

    elif opcao == "2":
        sistema.listar_barras()

    elif opcao == "3":
        sistema.adicionar_linha()

    elif opcao == "4":
        sistema.validar_grafo()

    elif opcao == "5":
        sistema.relatorio()

    elif opcao == "6":
        sistema.simular_estabilidade()

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida.\n")