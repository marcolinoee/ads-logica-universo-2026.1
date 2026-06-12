def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    else:
        return a / b
    
print(dividir(10, 2))
print(dividir(15, 0))