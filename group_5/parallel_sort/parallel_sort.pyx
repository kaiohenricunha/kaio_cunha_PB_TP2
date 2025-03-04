# parallel_sort.pyx
"""
Implementa a ordenação de uma lista usando MergeSort em versões sequencial e paralela.
Utiliza OpenMP via Cython para paralelizar as chamadas recursivas no MergeSort.
Para compilar com OpenMP, use o setup.py correspondente.
"""

import cython
from cython.parallel import prange
cimport cython
import numpy as np
cimport numpy as np

# Define um limiar para usar a versão sequencial para subarrays pequenos.
cdef int THRESHOLD = 1000

# Função para mesclar duas metades ordenadas do array.
cdef void merge(double[:] arr, double[:] temp, int left, int mid, int right) nogil:
    cdef int i = left, j = mid + 1, k = left, idx
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    while i <= mid:
        temp[k] = arr[i]
        i += 1; k += 1
    while j <= right:
        temp[k] = arr[j]
        j += 1; k += 1
    # Copia de volta para o array original.
    for idx in range(left, right + 1):
        arr[idx] = temp[idx]

# MergeSort sequencial recursivo.
cdef void sequential_mergesort(double[:] arr, double[:] temp, int left, int right) nogil:
    cdef int mid
    if left < right:
        mid = (left + right) // 2
        sequential_mergesort(arr, temp, left, mid)
        sequential_mergesort(arr, temp, mid + 1, right)
        merge(arr, temp, left, mid, right)

# MergeSort paralelo recursivo.
cdef void parallel_mergesort(double[:] arr, double[:] temp, int left, int right) nogil:
    cdef int mid, dummy
    if right - left < THRESHOLD:
        sequential_mergesort(arr, temp, left, right)
    else:
        mid = (left + right) // 2
        for dummy in prange(2, nogil=True, schedule="static"):
            if dummy == 0:
                parallel_mergesort(arr, temp, left, mid)
            else:
                parallel_mergesort(arr, temp, mid + 1, right)
        merge(arr, temp, left, mid, right)

# Função Python para ordenação sequencial.
def sequential_sort(np.ndarray[np.double_t, ndim=1] arr):
    cdef int n = arr.shape[0]
    cdef np.ndarray[np.double_t, ndim=1] temp = np.empty(n, dtype=np.double)
    with nogil:
        sequential_mergesort(arr, temp, 0, n - 1)
    return arr

# Função Python para ordenação paralela.
def parallel_sort(np.ndarray[np.double_t, ndim=1] arr):
    cdef int n = arr.shape[0]
    cdef np.ndarray[np.double_t, ndim=1] temp = np.empty(n, dtype=np.double)
    with nogil:
        parallel_mergesort(arr, temp, 0, n - 1)
    return arr

def main():
    """
    Testa e compara as versões sequencial e paralela do MergeSort.
    Gera arrays de tamanhos em potências de 2 (de ~1e3 até ~1e6 elementos),
    mede os tempos de execução e plota um gráfico comparativo.
    """
    import time
    import matplotlib.pyplot as plt
    import numpy as np

    sizes = [2**i for i in range(10, 21)]  # de 1024 até ~1 milhão de elementos
    seq_times = []
    par_times = []
    
    for size in sizes:
        arr_seq = np.random.rand(int(size)).astype(np.double)
        arr_par = arr_seq.copy()
        
        start = time.time()
        sequential_sort(arr_seq)
        seq_time = time.time() - start
        seq_times.append(seq_time)
        
        start = time.time()
        parallel_sort(arr_par)
        par_time = time.time() - start
        par_times.append(par_time)
        
        print(f"Tamanho: {size:8d} | Sequencial: {seq_time:.6f} s | Paralelo: {par_time:.6f} s")
    
    plt.figure()
    plt.plot(sizes, seq_times, marker='o', label="Sequencial")
    plt.plot(sizes, par_times, marker='o', label="Paralelo")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Tamanho do Array (log)")
    plt.ylabel("Tempo (s, log)")
    plt.title("MergeSort: Paralelo vs Sequencial")
    plt.legend()
    plt.grid(True)
    plt.savefig("grafico_ordenacao_paralela.png")
    plt.show()

if __name__ == "__main__":
    main()
