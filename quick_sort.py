import random
import time

def quicksort(arr, pivot_strategy="first"):
    """
    Ordena uma lista de números usando o algoritmo QuickSort.
    
    Parâmetros:
      arr: lista de números a ser ordenada.
      pivot_strategy: estratégia para escolher o pivô ('first', 'last' ou 'median').
      
    Retorna:
      Uma nova lista ordenada.
    """
    if len(arr) <= 1:
        return arr

    # Escolha do pivô de acordo com a estratégia
    if pivot_strategy == "first":
        pivot = arr[0]
    elif pivot_strategy == "last":
        pivot = arr[-1]
    elif pivot_strategy == "median":
        # Seleciona o pivô como a mediana entre o primeiro, o do meio e o último elemento
        first = arr[0]
        middle = arr[len(arr) // 2]
        last = arr[-1]
        pivot = sorted([first, middle, last])[1]
    else:
        raise ValueError("Estratégia de pivô inválida. Escolha 'first', 'last' ou 'median'.")

    # Particiona a lista em três partes: menores, iguais e maiores que o pivô
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Chamada recursiva
    return quicksort(left, pivot_strategy) + middle + quicksort(right, pivot_strategy)

def main():
    # Gera uma lista de 10.000 números aleatórios
    lista = [random.randint(0, 10000) for _ in range(10000)]
    
    pivot_strategies = ["first", "last", "median"]
    for strategy in pivot_strategies:
        start_time = time.time()
        sorted_list = quicksort(lista, pivot_strategy=strategy)
        elapsed = time.time() - start_time
        print(f"Estratégia do pivô: {strategy:6s} -> Tempo: {elapsed:.4f} s")
        # Verificação simples da ordenação
        if sorted_list != sorted(lista):
            print("Erro: a lista não está ordenada corretamente!")

if __name__ == "__main__":
    main()

