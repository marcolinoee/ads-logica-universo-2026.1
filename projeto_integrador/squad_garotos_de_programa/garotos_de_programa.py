# ==========================================
# ALUNO 3 - CLASSE TRANSACAO
# ==========================================

class Transacao:

    def __init__(self, codigo, valor, conta, responsavel):
        self.codigo = codigo
        self.valor = valor
        self.conta = conta
        self.responsavel = responsavel

    def obter_primeiro_digito(self):

        texto = str(self.valor)

        texto = texto.replace(".", "")
        texto = texto.replace("-", "")
        texto = texto.lstrip("0")

        if len(texto) > 0:
            return int(texto[0])

        return None


# ==========================================
# ALUNO 1 - INTERFACE DE LANÇAMENTOS
# ==========================================

class InterfaceLancamentos:

    def __init__(self):
        self.livro_diario = []

    def adicionar_transacao(
        self,
        codigo,
        valor,
        conta,
        responsavel
    ):

        if not isinstance(valor, (int, float)):
            print("Erro: valor inválido.")
            return

        if valor <= 0:
            print("Erro: valor deve ser maior que zero.")
            return

        nova = Transacao(
            codigo,
            valor,
            conta,
            responsavel
        )

        self.livro_diario.append(nova)

        print(
            f"Transação {codigo} cadastrada."
        )


# ==========================================
# ALUNO 2 - MOTOR ESTATÍSTICO
# ==========================================

class MotorEstatistico:

    @staticmethod
    def calcular_metricas(
        transacoes,
        conta_alvo
    ):

        valores = []

        for t in transacoes:

            if t.conta == conta_alvo:
                valores.append(t.valor)

        n = len(valores)

        if n == 0:
            return 0, 0, 0

        soma = 0

        for valor in valores:
            soma += valor

        media = soma / n

        soma_quadrados = 0

        for valor in valores:

            soma_quadrados += (
                (valor - media) ** 2
            )

        variancia = soma_quadrados / n

        desvio_padrao = variancia ** 0.5

        return (
            media,
            variancia,
            desvio_padrao
        )

    @staticmethod
    def detectar_outliers(
        transacoes,
        conta_alvo
    ):

        (
            media,
            variancia,
            desvio
        ) = MotorEstatistico.calcular_metricas(
            transacoes,
            conta_alvo
        )

        limite_superior = (
            media + (3 * desvio)
        )

        limite_inferior = (
            media - (3 * desvio)
        )

        suspeitas = []

        for t in transacoes:

            if t.conta == conta_alvo:

                if (
                    t.valor > limite_superior
                    or
                    t.valor < limite_inferior
                ):

                    suspeitas.append(t)

        return (
            suspeitas,
            media,
            variancia,
            desvio,
            limite_inferior,
            limite_superior
        )


# ==========================================
# ALUNO 3 - LEI DE BENFORD
# ==========================================

class MotorBenford:

    @staticmethod
    def analisar(transacoes):

        frequencia_teorica = {
            1: 30.1,
            2: 17.6,
            3: 12.5,
            4: 9.7,
            5: 7.9,
            6: 6.7,
            7: 5.8,
            8: 5.1,
            9: 4.6
        }

        contagem = {}

        for i in range(1, 10):
            contagem[i] = 0

        total = 0

        for t in transacoes:

            digito = (
                t.obter_primeiro_digito()
            )

            if digito is not None:

                contagem[digito] += 1
                total += 1

        frequencia_real = {}

        for i in range(1, 10):

            if total > 0:

                frequencia_real[i] = round(
                    (
                        contagem[i] / total
                    ) * 100,
                    1
                )

            else:

                frequencia_real[i] = 0

        return (
            frequencia_teorica,
            frequencia_real
        )


# ==========================================
# ALUNO 4 - RELATÓRIO
# ==========================================

class RelatorioCompliance:

    @staticmethod
    def gerar(
        transacoes,
        conta
    ):

        (
            suspeitas,
            media,
            variancia,
            desvio,
            limite_inferior,
            limite_superior
        ) = MotorEstatistico.detectar_outliers(
            transacoes,
            conta
        )

        print("\n" + "=" * 60)
        print("RELATÓRIO DE COMPLIANCE")
        print("=" * 60)

        print(
            f"\nConta analisada: {conta}"
        )

        print(
            f"Média: {media:.2f}"
        )

        print(
            f"Variância: {variancia:.2f}"
        )

        print(
            f"Desvio Padrão: {desvio:.2f}"
        )

        print(
            f"Faixa 3 Sigmas: "
            f"{limite_inferior:.2f} "
            f"até "
            f"{limite_superior:.2f}"
        )

        print("\nOUTLIERS:")

        if len(suspeitas) == 0:

            print(
                "Nenhuma transação fora "
                "dos limites."
            )

        else:

            for t in suspeitas:

                print(
                    f"ID: {t.codigo}"
                    f" | Valor: R$ {t.valor:.2f}"
                    f" | Responsável: {t.responsavel}"
                )

        print("\n" + "-" * 60)
        print("LEI DE BENFORD")
        print("-" * 60)

        (
            teorica,
            real
        ) = MotorBenford.analisar(
            transacoes
        )

        for d in range(1, 10):

            barra_real = (
                "■" * int(real[d] / 2)
            )

            barra_teorica = (
                "░" * int(teorica[d] / 2)
            )

            print(
                f"\nDígito {d}"
            )

            print(
                f"Real    : "
                f"{real[d]}% "
                f"{barra_real}"
            )

            print(
                f"Teórica : "
                f"{teorica[d]}% "
                f"{barra_teorica}"
            )

        print("\n" + "=" * 60)


# ==========================================
# TESTE DO SISTEMA
# ==========================================

sistema = InterfaceLancamentos()

sistema.adicionar_transacao(
    "T01",
    105,
    "Caixa",
    "Carlos"
)

sistema.adicionar_transacao(
    "T02",
    98,
    "Caixa",
    "Ana"
)

sistema.adicionar_transacao(
    "T03",
    110,
    "Caixa",
    "Mariana"
)

sistema.adicionar_transacao(
    "T04",
    102,
    "Caixa",
    "Carlos"
)

sistema.adicionar_transacao(
    "T05",
    950,
    "Caixa",
    "Robson"
)

sistema.adicionar_transacao(
    "T06",
    15,
    "Suprimentos",
    "Ana"
)

sistema.adicionar_transacao(
    "T07",
    450,
    "Equipamentos",
    "Mariana"
)

sistema.adicionar_transacao(
    "T08",
    120,
    "Suprimentos",
    "Carlos"
)

RelatorioCompliance.gerar(
    sistema.livro_diario,
    "Caixa"
)