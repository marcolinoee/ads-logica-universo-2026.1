# catalogo_poo.py by Antônio (AntonioOliveira-Web)

# CLASSES PARA CADA TIPO DE PRODUTO PARA CRIAR O CATALAGO
# Classe principal do sistema
class ProjetoFotovoltaico:
    def __init__(
        self,
        cliente,
        painel,
        inversor,
        bateria=None
    ):
        self.cliente    = cliente
        self.painel     = painel
        self.inversor   = inversor
        self.bateria    = bateria

        self.kwp_total          = 0
        self.qtd_paineis        = 0
        self.qtd_baterias       = 0
        self.custo_total        = 0
        self.economia_mensal    = 0
        self.payback            = 0


# Classe do painel solar
class PainelSolar:
    def __init__(self, modelo, potencia_kw, preco):
        self.modelo         = modelo
        self.potencia_kw    = potencia_kw
        self.preco          = preco

        
# Classe do inversor
class Inversor:
    def __init__(self, modelo, potencia_kw, preco):
        self.modelo         = modelo
        self.potencia_kw    = potencia_kw
        self.preco          = preco


# Classe da bateria
class Bateria:
    def __init__(self, modelo, capacidade_ah, tensao_v, preco):
        self.modelo         = modelo
        self.capacidade_ah  = capacidade_ah
        self.tensao_v       = tensao_v
        self.preco          = preco
        
# OBJETOS DO CATALOGO
paineis = [
    PainelSolar("Painel 450w", 0.45, 900),
    PainelSolar("Painel 550w", 0.55, 1200),
]

inversores = [
    Inversor("Inversor 3kw", 3, 4000),
    Inversor("Inversor 5kw", 5, 6000),
]

baterias = [
    Bateria("Bateria 150Ah 24V", 150, 24, 3500),
    Bateria("Bateria 200Ah 48V", 200, 48, 6000),
]
