from produtos import produtos


def processar_venda(codigo, quantidade):

    produto_encontrado = None


    # Procurar produto pelo código
    for produto in produtos:

        if produto.codigo == codigo:
            produto_encontrado = produto



    if produto_encontrado is None:

        print("Produto não encontrado!")
        return



    estoque = produto_encontrado.estoque_total()


    if quantidade > estoque:

        print("Estoque insuficiente!")
        return



    print("\n=== PROCESSANDO VENDA ===")


    # PEPS - Primeiro lote que entrou sai primeiro
    while quantidade > 0:


        lote_atual = produto_encontrado.lotes[0]



        if lote_atual.quantidade <= quantidade:


            quantidade -= lote_atual.quantidade


            print(
                f"Lote {lote_atual.codigo} removido"
            )


            produto_encontrado.lotes.pop(0)



        else:


            lote_atual.quantidade -= quantidade


            print(
                f"Baixa realizada no lote {lote_atual.codigo}"
            )


            quantidade = 0



    print("Venda realizada com sucesso!")

    print(
        "Estoque atual:",
        produto_encontrado.estoque_total()
    )