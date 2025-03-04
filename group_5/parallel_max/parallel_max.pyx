"""
Encontra o valor máximo de um array utilizando versões sequencial e paralela com OpenMP.
Para compilar com OpenMP, use o setup.py fornecido.
"""

import numpy as np
cimport numpy as np
from cython.parallel import prange, threadid
import time

def sequential_max(np.ndarray[np.int32_t, ndim=1] arr):
    """
    Encontra o valor máximo de 'arr' de forma sequencial.
    Complexidade: O(n)
    """
    cdef Py_ssize_t i, n = arr.shape[0]
    cdef int max_val = arr[0]
    for i in range(1, n):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

def parallel_max(np.ndarray[np.int32_t, ndim=1] arr):
    """
    Encontra o valor máximo de 'arr' de forma paralela.
    Cada thread calcula seu máximo parcial, que depois é combinado.
    """
    cdef Py_ssize_t i, n = arr.shape[0]
    # Número de threads a utilizar (ajuste conforme seu ambiente)
    cdef int nthreads = 4  
    # Vetor para armazenar os máximos parciais
    cdef np.ndarray[np.int32_t, ndim=1] partial_max = np.empty(nthreads, dtype=np.int32)
    cdef int tid  # declare antes do loop

    # Inicializa cada posição do vetor com o primeiro valor
    for i in range(nthreads):
        partial_max[i] = arr[0]
    
    # Loop paralelo: cada thread atualiza seu máximo parcial
    for i in prange(n, nogil=True, schedule="static"):
        tid = threadid()
        if arr[i] > partial_max[tid]:
            partial_max[tid] = arr[i]
    
    # Combina os resultados parciais
    cdef int max_val = partial_max[0]
    for i in range(1, nthreads):
        if partial_max[i] > max_val:
            max_val = partial_max[i]
    return max_val

def main():
    """
    Testa e compara as versões sequencial e paralela.
    Gera um array de 10 milhões de inteiros aleatórios.
    """
    import numpy as np
    import time
    n = 10_000_000  # 10 milhões de elementos
    np.random.seed(0)
    arr = np.random.randint(0, 100000, size=n).astype(np.int32)
    
    t0 = time.time()
    seq_max = sequential_max(arr)
    t_seq = time.time() - t0
    
    t0 = time.time()
    par_max = parallel_max(arr)
    t_par = time.time() - t0
    
    print("Sequencial max:", seq_max, "Tempo:", t_seq, "s")
    print("Paralelo max:   ", par_max, "Tempo:", t_par, "s")

if __name__ == "__main__":
    main()
