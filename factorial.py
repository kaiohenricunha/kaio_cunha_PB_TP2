def factorial(n):
    """
    Calcula o fatorial de n de forma recursiva.
    n deve ser um inteiro não-negativo.
    """
    if n < 0:
        raise ValueError("n deve ser não-negativo")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Teste da função factorial
if __name__ == "__main__":
    test_values = [0, 1, 5, 10]
    for val in test_values:
        print(f"Fatorial de {val} é {factorial(val)}")

