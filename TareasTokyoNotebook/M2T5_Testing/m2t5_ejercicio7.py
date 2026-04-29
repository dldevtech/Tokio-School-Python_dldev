def factorial(n: int) -> int:
    if n < 0:
        raise ValueError('n negativo')
    resultado = 1
    for i in range(2, n+1):
        resultado *= i
    return resultado