from collections import Counter

def permute_unique(s):
    """
    Gera todas as permutações únicas da string 's'.
    
    Utiliza recursão com backtracking e um contador para evitar duplicatas.
    
    Retorna:
      Uma lista com todas as permutações únicas.
      
    Complexidade: No pior caso, O(n! * n), onde n é o tamanho da string,
    já que são geradas n! permutações e cada permutação pode demandar O(n)
    para ser construída.
    """
    result = []
    counter = Counter(s)
    
    def backtrack(path):
        # Se o caminho (path) tiver o mesmo tamanho da string, uma permutação foi formada.
        if len(path) == len(s):
            result.append("".join(path))
            return
        # Itera sobre os caracteres disponíveis (ordenados para uma saída determinística).
        for char in sorted(counter.keys()):
            if counter[char] > 0:
                # Escolhe o caractere e diminui seu contador.
                path.append(char)
                counter[char] -= 1
                backtrack(path)
                # Backtrack: desfaz a escolha.
                path.pop()
                counter[char] += 1
                
    backtrack([])
    return result

def print_permutations(s):
    """
    Imprime todas as permutações únicas da string 's'.
    """
    perms = permute_unique(s)
    for p in perms:
        print(p)

# Teste da função com um exemplo
if __name__ == "__main__":
    test_str = "aabc"  # string com caracteres repetidos
    print(f"Permutações únicas para '{test_str}':")
    print_permutations(test_str)

