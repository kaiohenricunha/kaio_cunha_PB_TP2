def lcs(s1, s2):
    """
    Retorna uma tupla (comprimento, subsequência) representando
    o tamanho da LCS entre s1 e s2, bem como a própria subsequência.
    """
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruindo a subsequência comum a partir da tabela dp
    lcs_length = dp[m][n]
    subsequence = []
    
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            subsequence.append(s1[i-1])
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
    
    subsequence.reverse()
    return lcs_length, "".join(subsequence)

def main():
    s1 = "ABCBDAB"
    s2 = "BDCABA"
    length, seq = lcs(s1, s2)
    print("String 1:", s1)
    print("String 2:", s2)
    print("Tamanho da LCS:", length)
    print("Subsequência Comum:", seq)

if __name__ == "__main__":
    main()
