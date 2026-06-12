#  1. Qual erro acontece?

#  O programa gera um ZeroDivisionError.

#   2. Por que ele ocorre?

#   Em Python (e em matemática), não é possível dividir um número por zero.

#    Quando b == 0, o interpretador não consegue calcular o resultado e interrompe a execução.

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero não é permitida."
    return a / b

print(dividir(10, 2))   # funciona → 5.0
print(dividir(10, 0))   # mensagem amigável
