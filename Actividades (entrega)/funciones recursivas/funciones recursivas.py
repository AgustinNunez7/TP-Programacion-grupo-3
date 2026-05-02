
#1
def sumar_naturales(numero:int) -> int:
    if numero < 2:
        devolver = numero
    else:
        devolver = numero + sumar_naturales(numero-1)

    return devolver

#2
def calcular_potencia(base:int, exponente:int)-> int:
    if exponente == 1:
        devolver = base
    else:
        devolver = base * calcular_potencia(base,exponente - 1)

    return devolver

#3
def sumar_digitos(numero:int)-> int:
    if numero < 10:
        devolver = numero
    else:
        devolver = (numero % 10) + sumar_digitos(numero // 10)

    return devolver

#4
def calcular_fibonacci(numero:int)-> int:
    if numero < 2:
        devolver = numero
    else:
        devolver = calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)

    return devolver

    
    