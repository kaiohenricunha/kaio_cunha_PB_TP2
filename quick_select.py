import random
import time

def quickselect(arr, k):
    """
    Retorna o k-ésimo menor elemento de 'arr'.
    k é 1-indexado, isto é, k=1 retorna o menor elemento.
    """
    if not arr:
        return None

    # Escolhe um pivô aleatório
    pivot = random.choice(arr)
    # Divide a lista em três partes
    left = [x for x in arr if x < pivot]
    pivots = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    if k <= len(left):
        return quickselect(left, k)
    elif k <= len(left) + len(pivots):
        # O pivô é o k-ésimo menor
        return pivot
    else:
        # Ajusta k para a parte 'right'
        return quickselect(right, k - len(left) - len(pivots))

def main():
    num_tests = 10
    list_size = 10000

    for test in range(1, num_tests+1):
        # Gera uma lista com 10.000 números entre 1 e 1000
        arr = [random.randint(1, 1000) for _ in range(list_size)]
        # Seleciona 5 valores de k aleatórios (1-indexados)
        ks = random.sample(range(1, list_size+1), 5)
        ks.sort()
        print(f"Teste {test}:")
        for k in ks:
            start = time.time()
            kth_element = quickselect(arr, k)
            elapsed = time.time() - start
            # Validação: compara com o resultado de uma ordenação completa
            kth_expected = sorted(arr)[k-1]
            correct = kth_element == kth_expected
            print(f"  k = {k:5d} -> QuickSelect: {kth_element:4d} | Sorted: {kth_expected:4d} | Correto? {correct} (Tempo: {elapsed:.4f} s)")
        print()

if __name__ == "__main__":
    main()

