from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_memoized(n):
    """
    Retorna o n-ésimo número da sequência de Fibonacci com memorização.
    n deve ser um inteiro não-negativo.
    """
    if n < 0:
        raise ValueError("n deve ser não-negativo")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)

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

# Teste comparativo entre versões
import time

if __name__ == "__main__":
    n = 35  # número grande para evidenciar a diferença
    print("\nComparando tempo de execução para Fibonacci:")

    start = time.time()
    result_recursive = fibonacci_recursive(n)
    end = time.time()
    print(f"Recursivo Simples: Fibonacci({n}) = {result_recursive} em {end - start:.4f} s")

    start = time.time()
    result_memoized = fibonacci_memoized(n)
    end = time.time()
    print(f"Memoized: Fibonacci({n}) = {result_memoized} em {end - start:.4f} s")
