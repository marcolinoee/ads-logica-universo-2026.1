# Depuracao de erro de execucao

# Código corrigido
def dividir(a, b):
    if b == 0:
        return "Nao é possivel dividir por zero."
    else:
        return a / b

print(dividir(10, 2))

# Acontece um erro pois em pyhton não é permitido dividir por zero
# A mensagem de erro que aparece é "ZeroDivisionError: division by zero"