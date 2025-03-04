def count_ways_to_paint(n, k):
    """
    Retorna o número de maneiras de pintar n cadeiras com k cores,
    de modo que cadeiras adjacentes não tenham a mesma cor.
    
    Utiliza um raciocínio de programação dinâmica:
    
    - dp[i] armazena o número de formas de pintar i cadeiras.
    - Se i == 1, temos k opções (cada cadeira pode ser de uma das k cores).
    - Se i >= 2, a quantidade de maneiras de pintar a cadeira i
      é (k-1) vezes a quantidade de maneiras de pintar i-1 cadeiras,
      pois a nova cadeira não pode ter a mesma cor da (i-1)-ésima.
      
    Em resumo, dp[1] = k e dp[i] = (k-1) * dp[i-1] para i >= 2.
    
    Complexidade: O(n), pois percorremos de 1 até n para calcular dp[i].
    """
    if n == 0:
        return 0
    if n == 1:
        return k
    
    # dp[i] = número de maneiras de pintar i cadeiras
    dp = [0] * (n+1)
    dp[1] = k
    dp[2] = k * (k-1)  # Se há pelo menos 2 cadeiras
    
    for i in range(3, n+1):
        dp[i] = (k-1) * dp[i-1]
    
    return dp[n]

def main():
    # Exemplo 1: 5 cadeiras, 3 cores
    n1, k1 = 5, 3
    ways1 = count_ways_to_paint(n1, k1)
    print(f"{n1} cadeiras, {k1} cores:")
    print("Maneiras de pintar (sem adjacentes iguais):", ways1)
    
    # Exemplo 2: 10 cadeiras, 2 cores
    n2, k2 = 10, 2
    ways2 = count_ways_to_paint(n2, k2)
    print(f"\n{n2} cadeiras, {k2} cores:")
    print("Maneiras de pintar (sem adjacentes iguais):", ways2)

if __name__ == "__main__":
    main()
