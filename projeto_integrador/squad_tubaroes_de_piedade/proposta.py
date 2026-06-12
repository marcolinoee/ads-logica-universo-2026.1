# proposta.py by Juan (Iz4nmura)

# Função que imprime o relatório
def imprimir_relatorio(projeto, mao_obra, tipo_sistema):
    # Desempacota os atributos do objeto para facilitar a leitura
    nome_cliente    = projeto.cliente
    painel          = projeto.painel
    inversor        = projeto.inversor
    bateria         = projeto.bateria
    kwp_total       = projeto.kwp_total
    qtd_paineis     = projeto.qtd_paineis
    qtd_baterias    = projeto.qtd_baterias
    economia_mensal = projeto.economia_mensal
    payback         = projeto.payback
    custo_total     = projeto.custo_total

    # Cálculo dos custos individuais
    custo_paineis   = qtd_paineis * painel.preco
    custo_inversor  = inversor.preco
    custo_baterias  = qtd_baterias * bateria.preco if bateria else 0

    # Converte payback de meses para anos e meses (para o rodapé)
    anos_payback    = int(payback) // 12
    meses_payback   = round(payback % 12)


    # ==================== CABEÇALHO ====================
    print("\n" + "=" * 45)
    print(f"{'EMPRESA SOLAR DOS ALUNOS':^45}")
    print(f"{'PROPOSTA COMERCIAL':^45}")
    print("=" * 45)

    print(f"{'Cliente:':<20} {nome_cliente}")
    print(f"{'Sistema:':<20} {tipo_sistema}")

    # ==================== DIMENSIONAMENTO ====================
    print("-" * 45)
    print(f"{'DIMENSIONAMENTO':^45}")
    print("-" * 45)

    print(f"{'Painel:':<20} {painel.modelo}")
    print(f"{'Potência (kWp):':<20} {kwp_total:.2f} kWp")
    print(f"{'Qtd. Painéis:':<20} {qtd_paineis}")
    print(f"{'Inversor:':<20} {inversor.modelo}")

    # Exibe baterias apenas se for Off-Grid
    if bateria:
        print(f"{'Bateria:':<20} {bateria.modelo}")
        print(f"{'Qtd. Baterias:':<20} {qtd_baterias}")

    # ==================== ORÇAMENTO ====================
    print("-" * 45)
    print(f"{'ORÇAMENTO':^45}")
    print("-" * 45)

    print(f"{'Painéis:':<20} R$ {custo_paineis:.2f}")
    print(f"{'Inversor:':<20} R$ {custo_inversor:.2f}")

    if bateria:
        print(f"{'Baterias:':<20} R$ {custo_baterias:.2f}")

    print(f"{'Mão de Obra:':<20} R$ {mao_obra:.2f}")
    print("-" * 45)

    print(f"{'Custo Total:':<20} R$ {custo_total:.2f}")
    print(f"{'Economia Mensal:':<20} R$ {economia_mensal:.2f}")

    # ==================== RODAPÉ ====================
    print("=" * 45)

    if payback is None:
        print("Payback: Não calculável")

    if anos_payback > 0:
        print(f"{'Payback:':<20} {int(payback)} meses ")
        print(f"({anos_payback} ano(s) e {meses_payback} mês/meses)")
    else:
        print(f"{'Payback:':<20} {payback:.1f} meses")

    print("=" * 45)
