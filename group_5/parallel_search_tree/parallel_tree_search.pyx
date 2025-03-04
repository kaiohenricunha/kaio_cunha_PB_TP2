# parallel_tree_search.pyx
# Para compilar com OpenMP, use o setup.py adequado.
from libc.stdlib cimport malloc
from cython.parallel import prange
cimport cython

# Definição de uma estrutura C para representar os nós da árvore.
cdef struct Node:
    int value
    Node* left
    Node* right

# Função recursiva (nogil) para construir uma árvore binária balanceada
# a partir de um array de inteiros (usando índices).
cdef Node* create_tree(int* data, int start, int end) nogil:
    cdef Node* root
    cdef int mid
    if start > end:
        return NULL
    mid = (start + end) // 2
    root = <Node*> malloc(sizeof(Node))
    if not root:
        return NULL
    root.value = data[mid]
    root.left = create_tree(data, start, mid - 1)
    root.right = create_tree(data, mid + 1, end)
    return root

# Função que constrói a árvore a partir de um array Python (ordenado)
cdef Node* build_tree_from_array(int[:] arr) nogil:
    cdef int n = arr.shape[0]
    cdef int* data = &arr[0]
    return create_tree(data, 0, n - 1)

# Função recursiva paralela para buscar um valor na árvore.
# Ela utiliza prange para buscar as duas subárvores em paralelo.
cdef int parallel_tree_search(Node* root, int target) nogil:
    if root == NULL:
        return 0
    if root.value == target:
        return 1

    cdef int results[2]
    cdef int i
    # Usa prange para criar duas tarefas: buscar na subárvore esquerda e direita.
    for i in prange(2, nogil=True, schedule="static"):
        if i == 0:
            results[i] = parallel_tree_search(root.left, target)
        else:
            results[i] = parallel_tree_search(root.right, target)
    return results[0] or results[1]

@cython.boundscheck(False)
@cython.wraparound(False)
def search_in_tree(int[:] arr, int target):
    """
    Função Python que:
      1. Constrói uma árvore binária balanceada a partir de um array ordenado.
      2. Busca, de forma paralela (usando OpenMP), o valor 'target' na árvore.
    Retorna True se o valor for encontrado e False caso contrário.
    """
    cdef Node* root
    root = build_tree_from_array(arr)
    cdef int found = parallel_tree_search(root, target)
    # Para simplificação, não liberamos a memória alocada.
    return bool(found)

def performance_test():
    """
    Testa a busca em árvore para tamanhos em potências de 2 (nós: 1, 2, 4, 8, ...).
    Mede e exibe o tempo de execução para a busca de um valor que está presente.
    """
    import time
    import matplotlib.pyplot as plt

    tree_sizes = []
    times = []
    # Testa para tamanhos de árvore de 2^i nós, para i de 0 a 16 (aprox. 65 mil nós).
    for i in range(0, 17):
        n = 2**i
        tree_sizes.append(n)
        # Cria um array ordenado de tamanho n: [0, 1, 2, ..., n-1]
        import numpy as np
        arr = np.arange(n, dtype=np.int32)
        # Busca por um valor garantidamente presente (por exemplo, n-1)
        target = n - 1
        start = time.time()
        found = search_in_tree(arr, target)
        elapsed = time.time() - start
        times.append(elapsed)
        print(f"Nós: {n:6d} | Valor buscado: {target:6d} | Encontrado: {found} | Tempo: {elapsed:.6f} s")
    # Plota o gráfico
    plt.figure()
    plt.plot(tree_sizes, times, marker="o")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Número de Nós (escala log)")
    plt.ylabel("Tempo de Busca (s, escala log)")
    plt.title("Busca Paralela em Árvore Binária com OpenMP")
    plt.grid(True)
    plt.savefig("grafico_busca_arvore.png")
    plt.show()
