def coin_change(coins, amount):
    """
    Retorna o número mínimo de moedas necessárias para formar 'amount'
    utilizando as moedas em 'coins'. Caso não seja possível, retorna -1.
    
    Utiliza programação dinâmica (abordagem bottom-up).
    
    Complexidade: O(len(coins) * amount)
    """
    # dp[i] guardará o número mínimo de moedas para formar o valor i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # zero moedas para formar valor 0

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] != float('inf'):
                dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

def main():
    # Exemplo 1
    coins1 = [1, 5, 10, 25]
    amount1 = 30
    result1 = coin_change(coins1, amount1)
    print("Conjunto de moedas:", coins1)
    print("Valor desejado:", amount1)
    print("Mínimo de moedas:", result1 if result1 != -1 else "Impossível")

    print()

    # Exemplo 2
    coins2 = [2, 6, 9]
    amount2 = 13
    result2 = coin_change(coins2, amount2)
    print("Conjunto de moedas:", coins2)
    print("Valor desejado:", amount2)
    print("Mínimo de moedas:", result2 if result2 != -1 else "Impossível")

    print()

    # Exemplo 3
    coins3 = [3, 4, 7]
    amount3 = 2
    result3 = coin_change(coins3, amount3)
    print("Conjunto de moedas:", coins3)
    print("Valor desejado:", amount3)
    print("Mínimo de moedas:", result3 if result3 != -1 else "Impossível")

if __name__ == "__main__":
    main()
