from produtos import produtos


def calcular_valor_total_estoque():

    valor_total = 0

    for produto in produtos:
        valor_total += produto.valor_estoque()

    return valor_total



def curva_abc():

    if len(produtos) == 0:
        print("Nenhum produto cadastrado!")
        return


    lista_ordenada = produtos.copy()


    lista_ordenada.sort(
        key=lambda produto: produto.valor_estoque(),
        reverse=True
    )


    valor_total = calcular_valor_total_estoque()


    acumulado = 0


    print("\n========== CURVA ABC ==========")


    for produto in lista_ordenada:


        valor = produto.valor_estoque()

        acumulado += valor


        percentual = (
            acumulado / valor_total
        ) * 100



        if percentual <= 70:
            produto.classe_abc = "A"


        elif percentual <= 90:
            produto.classe_abc = "B"


        else:
            produto.classe_abc = "C"



        print("--------------------------------")
        print("Produto:", produto.nome)
        print("Valor estoque: R$", valor)
        print("Classe:", produto.classe_abc)



    print("--------------------------------")
    print("Valor total armazenado: R$", valor_total)




def relatorio_estoque_minimo():


    print("\n======= ESTOQUE MÍNIMO =======")


    encontrou = False


    for produto in produtos:


        estoque = produto.estoque_total()


        if estoque < produto.estoque_minimo:


            encontrou = True


            print("-----------------------------")
            print("Produto:", produto.nome)
            print("Estoque atual:", estoque)
            print("Estoque mínimo:", produto.estoque_minimo)
            print("AÇÃO: Comprar produto")



    if encontrou == False:

        print("Nenhum produto precisa de reposição.")





def inventario_geral():


    print("\n========= INVENTÁRIO =========")


    if len(produtos) == 0:

        print("Nenhum produto cadastrado.")
        return



    for produto in produtos:


        print("-----------------------------")

        print("Código:", produto.codigo)

        print("Produto:", produto.nome)

        print(
            "Quantidade:",
            produto.estoque_total()
        )

        print(
            "Valor:",
            produto.valor_estoque()
        )

        print(
            "Classe ABC:",
            produto.classe_abc
        )




def relatorio_lotes():


    print("\n========== LOTES ==========")


    for produto in produtos:


        print("\nProduto:", produto.nome)


        for lote in produto.lotes:


            print("----------------")

            print("Lote:", lote.codigo)

            print("Validade:", lote.validade)

            print(
                "Quantidade:",
                lote.quantidade
            )