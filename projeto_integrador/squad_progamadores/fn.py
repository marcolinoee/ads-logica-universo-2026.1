# ============================================================
# SISTEMA DE ANÁLISE FINANCEIRA EMPRESARIAL
# PROJETO FACULDADE - POO + LÓGICA PURA
# ============================================================


# ============================================================
# 1. CLASSE BASE - DEMONSTRAÇÃO FINANCEIRA
# ============================================================

class DemonstracaoFinanceira:

    def __init__(self, ano, ac, ai, pc, pnc, pl, rl, lb, ll, caixa, estoques):

        # Dados principais
        self.ano = ano
        self.ac = ac
        self.ai = ai
        self.pc = pc
        self.pnc = pnc
        self.pl = pl

        # Resultado
        self.rl = rl
        self.lb = lb
        self.ll = ll

        # Contas auxiliares
        self.caixa = caixa
        self.estoques = estoques

        # Totais
        self.ativo_total = self.ac + self.ai
        self.passivo_total = self.pc + self.pnc + self.pl

        # Indicadores
        self.liquidez_corrente = 0
        self.liquidez_seca = 0
        self.liquidez_imediata = 0
        self.endividamento_geral = 0
        self.roe = 0
        self.margem_liquida = 0

        # Análise vertical
        self.margem_bruta = 0
        self.peso_estoques = 0


# ============================================================
# 2. MOTOR ANALÍTICO
# ============================================================

class MotorAnalitico:

    def calcular_indicadores(self, df):

        # Liquidez corrente
        if df.pc > 0:
            df.liquidez_corrente = df.ac / df.pc
        else:
            df.liquidez_corrente = 0

        # Liquidez seca
        if df.pc > 0:
            df.liquidez_seca = (df.ac - df.estoques) / df.pc
        else:
            df.liquidez_seca = 0

        # Liquidez imediata
        if df.pc > 0:
            df.liquidez_imediata = df.caixa / df.pc
        else:
            df.liquidez_imediata = 0

        # Endividamento geral
        if df.ativo_total > 0:
            df.endividamento_geral = (df.pc + df.pnc) / df.ativo_total
        else:
            df.endividamento_geral = 0

        # ROE
        if df.pl > 0:
            df.roe = df.ll / df.pl
        else:
            df.roe = 0

        # Margem líquida
        if df.rl > 0:
            df.margem_liquida = df.ll / df.rl
        else:
            df.margem_liquida = 0

        # Análise vertical
        if df.rl > 0:
            df.margem_bruta = df.lb / df.rl
        else:
            df.margem_bruta = 0

        if df.ativo_total > 0:
            df.peso_estoques = df.estoques / df.ativo_total
        else:
            df.peso_estoques = 0


# ============================================================
# 3. GERENCIADOR DE EMPRESA (HISTÓRICO)
# ============================================================

class GerenciadorEmpresa:

    def __init__(self):
        self.historico = []

    def adicionar(self, df):

        if len(self.historico) == 5:
            self.historico.pop(0)

        self.historico.append(df)

    def ultimo_ano(self):

        if len(self.historico) > 0:
            return self.historico[len(self.historico) - 1]
        else:
            return None


# ============================================================
# 4. DIAGNÓSTICO FINANCEIRO
# ============================================================

class DiagnosticoFinanceiro:

    def calcular_score(self, df):

        score = 0

        # Liquidez
        if df.liquidez_corrente >= 1.5:
            score = score + 2
        elif df.liquidez_corrente >= 1:
            score = score + 1

        # ROE
        if df.roe >= 0.10:
            score = score + 2
        elif df.roe >= 0.05:
            score = score + 1

        # Endividamento
        if df.endividamento_geral <= 0.5:
            score = score + 2
        elif df.endividamento_geral <= 0.7:
            score = score + 1

        return score

    def interpretar_liquidez(self, v):

        if v < 1:
            return "ALERTA CRÍTICO"
        elif v < 1.5:
            return "REGULAR"
        else:
            return "SAUDÁVEL"

    def interpretar_endividamento(self, v):

        if v > 0.7:
            return "ALTO RISCO"
        elif v > 0.5:
            return "ATENÇÃO"
        else:
            return "CONTROLADO"

    def interpretar_roe(self, v):

        if v > 0.15:
            return "EXCELENTE"
        elif v > 0.10:
            return "BOM"
        else:
            return "BAIXO"


# ============================================================
# 5. DASHBOARD
# ============================================================

class Dashboard:

    def exibir(self, historico):

        print("\n" + "=" * 90)
        print("DASHBOARD FINANCEIRO".center(90))
        print("=" * 90)

        print("ANO | LC | LS | LI | EG | ROE | ML | STATUS")
        print("-" * 90)

        i = 0

        while i < len(historico):

            df = historico[i]

            if df.liquidez_corrente >= 1.5 and df.roe >= 0.10:
                status = "EXCELENTE"
            elif df.liquidez_corrente >= 1:
                status = "OK"
            else:
                status = "ALERTA"

            print(
                str(df.ano) + " | " +
                str(round(df.liquidez_corrente, 2)) + " | " +
                str(round(df.liquidez_seca, 2)) + " | " +
                str(round(df.liquidez_imediata, 2)) + " | " +
                str(round(df.endividamento_geral, 2)) + " | " +
                str(round(df.roe * 100, 1)) + "% | " +
                str(round(df.margem_liquida * 100, 1)) + "% | " +
                status
            )

            i = i + 1

        print("=" * 90)


# ============================================================
# 6. INTERFACE (MENU PRINCIPAL)
# ============================================================

class Interface:

    def __init__(self):

        self.empresa = GerenciadorEmpresa()
        self.motor = MotorAnalitico()
        self.diagnostico = DiagnosticoFinanceiro()
        self.dashboard = Dashboard()

    def iniciar(self):

        while True:

            print("\n======================================")
            print("SISTEMA FINANCEIRO EMPRESARIAL")
            print("======================================")

            print("1 - Inserir Dados")
            print("2 - Dashboard")
            print("3 - Diagnóstico")
            print("4 - Sair")

            op = input("Escolha: ")

            # Inserção
            if op == "1":

                ano = int(input("Ano: "))
                ac = float(input("AC: "))
                ai = float(input("AI: "))
                pc = float(input("PC: "))
                pnc = float(input("PNC: "))
                pl = float(input("PL: "))
                rl = float(input("RL: "))
                lb = float(input("LB: "))
                ll = float(input("LL: "))
                caixa = float(input("Caixa: "))
                estoques = float(input("Estoques: "))

                df = DemonstracaoFinanceira(
                    ano, ac, ai, pc, pnc, pl,
                    rl, lb, ll, caixa, estoques
                )

                self.motor.calcular_indicadores(df)
                self.empresa.adicionar(df)

                print("✔ Dados cadastrados!")

            # Dashboard
            elif op == "2":

                if len(self.empresa.historico) == 0:
                    print("Sem dados.")
                else:
                    self.dashboard.exibir(self.empresa.historico)

            # Diagnóstico
            elif op == "3":

                ultimo = self.empresa.ultimo_ano()

                if ultimo == None:
                    print("Sem dados.")
                else:

                    score = self.diagnostico.calcular_score(ultimo)

                    print("\n--- DIAGNÓSTICO ---")
                    print("Liquidez:", self.diagnostico.interpretar_liquidez(ultimo.liquidez_corrente))
                    print("Endividamento:", self.diagnostico.interpretar_endividamento(ultimo.endividamento_geral))
                    print("ROE:", self.diagnostico.interpretar_roe(ultimo.roe))
                    print("SCORE:", score, "/ 6")

            elif op == "4":
                print("Encerrando...")
                break

            else:
                print("Opção inválida")


# ============================================================
# EXECUÇÃO DO SISTEMA
# ============================================================

sistema = Interface()
sistema.iniciar()
