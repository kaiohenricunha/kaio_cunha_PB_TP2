def knapsack_0_1(items, capacity):
    """
    Resolve o problema da mochila 0-1 usando programação dinâmica.

    Parâmetros:
    - items: lista de tuplas (peso, valor)
    - capacity: capacidade máxima da mochila

    Retorna:
    - O valor máximo que pode ser transportado na mochila.
    
    Complexidade de tempo: O(n * capacity),
    onde n é o número de itens e capacity é o peso máximo.
    """
    n = len(items)
    # dp[i][w] representará o valor máximo possível usando até os i primeiros itens
    # com capacidade w.
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        peso_atual, valor_atual = items[i - 1]  # índice do item na lista
        for w in range(capacity + 1):
            if peso_atual > w:
                # Não é possível incluir este item se o peso excede w
                dp[i][w] = dp[i - 1][w]
            else:
                # Podemos escolher não incluir (dp[i-1][w])
                # ou incluir (dp[i-1][w - peso_atual] + valor_atual) se couber
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - peso_atual] + valor_atual)
    
    return dp[n][capacity]

def main():
    # Exemplo 1
    items1 = [(2, 3), (4, 6), (5, 9), (6, 12)]  # (peso, valor)
    capacity1 = 8
    max_val1 = knapsack_0_1(items1, capacity1)
    print("Exemplo 1:")
    print("Itens:", items1)
    print("Capacidade:", capacity1)
    print("Valor máximo:", max_val1)

    print()

    # Exemplo 2
    items2 = [(1, 1), (2, 6), (3, 10), (5, 15), (6, 18)]
    capacity2 = 10
    max_val2 = knapsack_0_1(items2, capacity2)
    print("Exemplo 2:")
    print("Itens:", items2)
    print("Capacidade:", capacity2)
    print("Valor máximo:", max_val2)

if __name__ == "__main__":
    main()
