from classes_poo import Produto, Lote


produtos = []



def cadastrar_produto():

    codigo = int(input("Código: "))
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    minimo = int(input("Estoque mínimo: "))


    produto = Produto(
        codigo,
        nome,
        preco,
        minimo
    )


    quantidade_lotes = int(
        input("Quantidade de lotes: ")
    )


    for i in range(quantidade_lotes):

        lote = input("Código do lote: ")

        validade = input("Validade: ")

        quantidade = int(
            input("Quantidade: ")
        )


        novo_lote = Lote(
            lote,
            validade,
            quantidade
        )


        produto.adicionar_lote(novo_lote)



    produtos.append(produto)

    print("Produto cadastrado!")