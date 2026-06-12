# Cores para o terminal para manter a interface intuitiva (Códigos ANSI nativos)
class Cores:
    AZUL = '\033[94m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    VERMELHO = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

class FatorEstrategico:
    def __init__(self, descricao, tipo, impacto):
        self.descricao = descricao
        self.tipo = tipo
        self.impacto = impacto

    def __str__(self):
        cor = Cores.VERDE if self.tipo in ["Força", "Oportunidade"] else Cores.AMARELO
        return f"{cor}• [{self.tipo.upper():^12}]{Cores.RESET} {self.descricao:<25} | Peso: {self.impacto}/5"

class ProblemaGUT:
    def __init__(self, descricao, g, u, t):
        self.descricao = descricao
        self.score = g * u * t
        self.detalhe = f"G:{g} U:{u} T:{t}"

    def __str__(self):
        aviso = Cores.VERMELHO + " [CRÍTICO]" if self.score > 60 else ""
        return f"{Cores.BOLD}Score: {self.score:>3}{Cores.RESET} | {self.descricao:<30} ({self.detalhe}){aviso}"

class PlanoAcao:
    def __init__(self, problema):
        self.problema = problema
        self.dados = {}
        
        perguntas = {
            "O QUE": ("Ação prática", "Ex: Trocar rolamentos"),
            "POR QUE": ("Justificativa", "Ex: Evitar travamento da máquina"),
            "QUEM": ("Responsável", "Ex: Técnico de Manutenção"),
            "QUANDO": ("Prazo final", "Ex: Próxima segunda-feira"),
            "ONDE": ("Local", "Ex: Linha de Produção A"),
            "COMO": ("Método", "Ex: Lubrificação e substituição"),
            "QUANTO": ("Custo", "Ex: R$ 200,00")
        }

        print(f"\n{Cores.AZUL}{Cores.BOLD}>>> PLANEJANDO SOLUÇÃO PARA: {problema.upper()}{Cores.RESET}")
        for chave, (rotulo, exemplo) in perguntas.items():
            valor = ""
            while not valor:
                valor = input(f" {Cores.BOLD}{chave}{Cores.RESET} ({rotulo}) [{Cores.AMARELO}{exemplo}{Cores.RESET}]: ")
                if not valor: print(f"{Cores.VERMELHO} Erro: Preenchimento obrigatório!{Cores.RESET}")
            self.dados[chave] = valor

    def exibir(self):
        print(f"\n{Cores.VERDE}┌──────────────────────────────────────────────────────────┐")
        print(f"│ FICHA DE AÇÃO: {self.problema[:40]:<41} │")
        print(f"├──────────────────────────────────────────────────────────┤")
        for k, v in self.dados.items():
            print(f"│ {k:<7}: {v[:47]:<48} │")
        print(f"└──────────────────────────────────────────────────────────┘{Cores.RESET}")

def limpar_tela():
    # Comando ANSI puro do Python para limpar a tela e resetar o cursor
    print("\033[H\033[J", end="")

def cabecalho(titulo):
    print(f"\n{Cores.AZUL}{'='*60}\n{titulo.center(60)}\n{'='*60}{Cores.RESET}")

def obter_nota(msg):
    while True:
        try:
            nota = int(input(f"  {msg} (1-5): "))
            if 1 <= nota <= 5: return nota
            print(f"{Cores.VERMELHO}  Digite uma nota válida entre 1 e 5!{Cores.RESET}")
        except ValueError:
            print(f"{Cores.VERMELHO}  Entrada inválida! Use apenas números.{Cores.RESET}")

# --- FUNÇÕES DE FASE ---

def fase_swot():
    cabecalho("FASE 1: IDENTIFICAÇÃO DE CENÁRIOS (SWOT)")
    fatores = []
    tipos = {"1": "Força", "2": "Fraqueza", "3": "Oportunidade", "4": "Ameaça"}
    
    while True:
        desc = input(f"\n{Cores.BOLD}Descreva o Problema ou Situação:{Cores.RESET} ")
        
        print(f"Como você classifica isso?")
        for k, v in tipos.items(): print(f"  {k}. {v}")
        
        t_idx = input("Opção (1-4): ")
        tipo = tipos.get(t_idx, "Outro")
        
        print(f"Qual o nível de impacto disso no negócio?")
        impacto = obter_nota("Nota de Impacto")
        
        fatores.append(FatorEstrategico(desc, tipo, impacto))
        
        continuar = input(f"\n{Cores.AMARELO}Deseja registrar mais algum ponto? (s/n): {Cores.RESET}").lower()
        if continuar != 's': break
    return fatores

def fase_gut():
    cabecalho("FASE 2: ANÁLISE DE PRIORIDADE (GUT)")
    problemas = []
    print(f"{Cores.AMARELO}Dica: Foque nos problemas que trazem mais risco imediato.{Cores.RESET}")
    
    while True:
        desc = input(f"\nQual problema/gargalo vamos priorizar agora? ")
        g = obter_nota("Gravidade (O quão sério é?)")
        u = obter_nota("Urgência (Isso pode esperar?)")
        t = obter_nota("Tendência (Piorará se nada for feito?)")
        
        problemas.append(ProblemaGUT(desc, g, u, t))
        if input(f"\n{Cores.AMARELO}Analisar outro problema? (s/n): {Cores.RESET}").lower() != 's': break
    
    # Ordenação nativa do Python usando função lambda
    problemas.sort(key=lambda x: x.score, reverse=True)
    return problemas

def main():
    limpar_tela()
    print(f"{Cores.BOLD}{Cores.AZUL}GERENCIADOR DE SOLUÇÕES ESTRATÉGICAS v3.1{Cores.RESET}")
    
    swot = fase_swot()
    limpar_tela()
    print(f"\n{Cores.BOLD}MAPA DE DIAGNÓSTICO:{Cores.RESET}")
    for f in swot: print(f)

    problemas = fase_gut()
    limpar_tela()
    print(f"\n{Cores.BOLD}RANKING DE PRIORIDADES (ORDEM DE ATUAÇÃO):{Cores.RESET}")
    for p in problemas: print(p)

    if problemas:
        cabecalho("FASE 3: ELABORAÇÃO DO PLANO DE RESPOSTA")
        # List comprehension (recurso nativo do Python) para focar nos 2 maiores problemas
        planos = [PlanoAcao(p.descricao) for p in problemas[:2]]
        
        limpar_tela()
        cabecalho("RELATÓRIO FINAL PARA EXECUÇÃO")
        for plano in planos:
            plano.exibir()
            
    print(f"\n{Cores.VERDE}✔ Processo concluído. Bom trabalho na execução!{Cores.RESET}\n")

if __name__ == "__main__":
    main()