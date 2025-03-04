import random

def partition(arr, low, high):
    """
    Função auxiliar que particiona o array em torno de um pivô.
    Todos os elementos menores que o pivô são movidos para a esquerda
    e os maiores para a direita.
    """
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quickselect_inplace(arr, low, high, k):
    """
    Implementa o QuickSelect de forma in-place para encontrar o k-ésimo
    menor elemento (índice k, onde k é 0-indexado).
    """
    if low == high:
        return arr[low]
    
    pivot_index = partition(arr, low, high)
    
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect_inplace(arr, low, pivot_index - 1, k)
    else:
        return quickselect_inplace(arr, pivot_index + 1, high, k)

def find_median(arr):
    """
    Encontra a mediana de 'arr' usando QuickSelect.
    Para tamanho ímpar, retorna o elemento central.
    Para tamanho par, retorna a média dos dois elementos centrais.
    """
    n = len(arr)
    if n % 2 == 1:
        # Cópia para não modificar a lista original
        arr_copy = arr[:]
        return quickselect_inplace(arr_copy, 0, n-1, n // 2)
    else:
        arr_copy1 = arr[:]  # Para o primeiro elemento da mediana
        arr_copy2 = arr[:]  # Para o segundo elemento da mediana
        median1 = quickselect_inplace(arr_copy1, 0, n-1, n // 2 - 1)
        median2 = quickselect_inplace(arr_copy2, 0, n-1, n // 2)
        return (median1 + median2) / 2.0

def find_k_smallest(arr, k):
    """
    Encontra os k menores elementos de 'arr' sem ordenar toda a lista.
    A função utiliza o QuickSelect para posicionar o k-ésimo menor elemento
    na posição k-1. Os k menores elementos ficam nas posições 0 até k-1 (não necessariamente ordenados).
    """
    arr_copy = arr[:]
    # Posiciona o k-ésimo menor elemento em arr_copy[k-1]
    quickselect_inplace(arr_copy, 0, len(arr_copy) - 1, k - 1)
    # Retorna os k primeiros elementos (pode ser opcionalmente ordenado se desejado)
    return arr_copy[:k]

def main():
    # Gera uma lista de 20 números aleatórios para demonstração
    data = [random.randint(1, 1000) for _ in range(20)]
    print("Lista:", data)
    
    # Encontra a mediana usando QuickSelect
    median = find_median(data)
    print("Mediana:", median)
    
    # Encontra os 5 menores elementos da lista
    k = 5
    k_smallest = find_k_smallest(data, k)
    print(f"{k} menores elementos (não necessariamente ordenados):", k_smallest)

if __name__ == "__main__":
    main()

