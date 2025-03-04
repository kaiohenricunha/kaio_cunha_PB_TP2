def fibonacci_recursive(n):
    """
    Retorna o n-ésimo número da sequência de Fibonacci de forma recursiva.
    n deve ser um inteiro não-negativo.
    """
    if n < 0:
        raise ValueError("n deve ser não-negativo")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Teste da versão recursiva simples
if __name__ == "__main__":
    print("\nFibonacci Recursivo Simples:")
    for i in range(10):
        print(f"Fibonacci({i}) = {fibonacci_recursive(i)}")
