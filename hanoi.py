import time
import matplotlib.pyplot as plt

def hanoi(n, source, target, auxiliary, print_moves=True):
    """
    Resolve o problema das Torres de Hanói para 'n' discos.
    
    Se print_moves for True, imprime cada movimento.
    Retorna o número de movimentos realizados.
    """
    if n == 1:
        if print_moves:
            print(f"Mova o disco 1 de {source} para {target}")
        return 1

    moves = 0
    # Move n-1 discos da origem para o auxiliar, usando o destino como auxiliar
    moves += hanoi(n - 1, source, auxiliary, target, print_moves)
    # Move o disco n da origem para o destino
    if print_moves:
        print(f"Mova o disco {n} de {source} para {target}")
    moves += 1
    # Move os n-1 discos do auxiliar para o destino, usando a origem como auxiliar
    moves += hanoi(n - 1, auxiliary, target, source, print_moves)
    return moves

def performance_test(max_disks=20):
    """
    Executa a função hanoi para n variando de 1 até max_disks (não imprime os movimentos)
    e mede o tempo de execução. Retorna duas listas: números de discos e tempos.
    """
    disk_counts = []
    times = []
    for n in range(1, max_disks + 1):
        start = time.time()
        moves = hanoi(n, 'A', 'C', 'B', print_moves=False)
        elapsed = time.time() - start
        disk_counts.append(n)
        times.append(elapsed)
        print(f"Discos: {n:2d} | Movimentos: {moves:12d} | Tempo: {elapsed:.4f} s")
    return disk_counts, times

def plot_performance(disk_counts, times):
    """Plota o gráfico de número de discos x tempo de execução."""
    plt.figure()
    plt.plot(disk_counts, times, marker="o")
    plt.title("Torres de Hanói: Número de Discos x Tempo de Execução")
    plt.xlabel("Número de Discos")
    plt.ylabel("Tempo (s)")
    plt.grid(True)
    plt.savefig("grafico_torres_hanoi.png")
    plt.show()

def main():
    print("=== Torres de Hanói: Exemplo com 3 discos (movimentos impressos) ===")
    hanoi(3, 'A', 'C', 'B', print_moves=True)
    
    print("\n=== Teste de desempenho (movimentos não são impressos) ===")
    # Para evitar tempos muito longos, altere max_disks se necessário.
    max_disks = 20  # experimente com 20; para 30, o tempo pode ser muito alto
    disk_counts, times = performance_test(max_disks)
    plot_performance(disk_counts, times)
    
    print("\nComplexidade do algoritmo: O(2ⁿ) (exponencial)")

if __name__ == "__main__":
    main()

