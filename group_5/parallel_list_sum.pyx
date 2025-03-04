# parallel_list_sum.pyx
"""
Soma de Elementos em uma Lista utilizando OpenMP.
Utilize este módulo com Cython para compilar com suporte a OpenMP.
O módulo define duas funções:
- sequential_sum: soma todos os elementos de forma sequencial.
- parallel_sum: utiliza prange e um vetor de somas parciais para paralelizar a soma.
A função main() gera um vetor grande, calcula as somas sequencial e paralelamente e compara os tempos.
"""

import numpy as np
cimport numpy as np
from cython.parallel import prange, threadid
import time

def sequential_sum(np.ndarray[np.int32_t, ndim=1] arr):
    """
    Soma todos os elementos de 'arr' de forma sequencial.
    """
    cdef Py_ssize_t i, n = arr.shape[0]
    cdef long total = 0
    for i in range(n):
        total += arr[i]
    return total

def parallel_sum(np.ndarray[np.int32_t, ndim=1] arr):
    """
    Soma todos os elementos de 'arr' de forma paralela utilizando OpenMP.
    A soma é realizada com um vetor de somas parciais, onde cada thread acumula sua parcela.
    """
    cdef Py_ssize_t i, n = arr.shape[0]
    cdef long total = 0
    # Determine um número de threads razoável.
    # Aqui, usamos 4 threads; em ambientes reais, pode-se usar omp_get_max_threads.
    cdef int nthreads = 4  
    # Cria um vetor para armazenar as somas parciais.
    cdef np.ndarray[np.int64_t, ndim=1] partial_sums = np.zeros(nthreads, dtype=np.int64)
    
    # A execução paralela: cada thread acumula sua parcela
    for i in prange(n, nogil=True, schedule='static'):
        partial_sums[threadid()] += arr[i]
    
    # Soma os valores parciais
    for i in range(nthreads):
        total += partial_sums[i]
    return total

def main():
    # Gera uma lista de 10 milhões de inteiros aleatórios
    cdef int size = 10000000
    np.random.seed(0)
    arr = np.random.randint(1, 100, size=size).astype(np.int32)
    
    # Soma Sequencial
    t_start = time.time()
    seq_result = sequential_sum(arr)
    t_seq = time.time() - t_start

    # Soma Paralela
    t_start = time.time()
    par_result = parallel_sum(arr)
    t_par = time.time() - t_start

    print("Soma Sequencial:", seq_result, "Tempo:", t_seq, "s")
    print("Soma Paralela:  ", par_result, "Tempo:", t_par, "s")

if __name__ == "__main__":
    main()
