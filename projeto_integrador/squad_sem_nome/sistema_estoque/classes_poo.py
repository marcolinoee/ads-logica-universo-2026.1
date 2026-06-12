class Lote:

    def __init__(self, codigo, validade, quantidade):
        self.codigo = codigo
        self.validade = validade
        self.quantidade = quantidade



class Produto:

    def __init__(self, codigo, nome, preco, estoque_minimo):

        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.estoque_minimo = estoque_minimo

        self.lotes = []

        self.classe_abc = ""



    def adicionar_lote(self, lote):

        self.lotes.append(lote)



    def estoque_total(self):

        total = 0

        for lote in self.lotes:
            total += lote.quantidade

        return total



    def valor_estoque(self):

        return self.estoque_total() * self.preco