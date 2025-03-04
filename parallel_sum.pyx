"""
Soma os elementos de um vetor em paralelo usando redução manual.
Crie um vetor com 10000 números aleatórios (entre 1 e 100000),
calcule a soma de forma sequencial e paralela, e compare os tempos.
"""

import numpy as np
cimport numpy as np
from cython.parallel import prange, threadid
import time

def sequential_sum(np.ndarray[np.int32_t, ndim=1] arr):
    cdef Py_ssize_t i, n = arr.shape[0]
    cdef long total = 0
    for i in range(n):
        total += arr[i]
    return total

def parallel_sum_manual(np.ndarray[np.int32_t, ndim=1] arr):
    """
    Soma os elementos de 'arr' em paralelo utilizando um vetor
    de somas parciais, onde cada thread acumula sua parcela.
    """
    cdef Py_ssize_t i, n = arr.shape[0]
    # Determina o número de threads a serem usadas; aqui usamos 4, mas pode ser ajustado.
    cdef int nthreads = 4  
    # Cria um vetor para armazenar as somas parciais (usamos int64 para evitar overflow)
    cdef np.ndarray[np.int64_t, ndim=1] partial_sums = np.zeros(nthreads, dtype=np.int64)
    
    for i in prange(n, nogil=True, schedule='static'):
        partial_sums[threadid()] += arr[i]
    
    cdef long total = 0
    for i in range(nthreads):
        total += partial_sums[i]
    return total

def main():
    cdef int size = 10000
    np.random.seed(0)
    # Cria um vetor de 10000 números aleatórios entre 1 e 100000
    arr = np.random.randint(1, 100001, size=size).astype(np.int32)
    
    # Soma sequencial
    t_start = time.time()
    seq = sequential_sum(arr)
    t_seq = time.time() - t_start

    # Soma paralela manual
    t_start = time.time()
    par = parallel_sum_manual(arr)
    t_par = time.time() - t_start

    print("Soma sequencial:", seq, "Tempo:", t_seq, "s")
    print("Soma paralela:  ", par, "Tempo:", t_par, "s")

if __name__ == '__main__':
    main()
