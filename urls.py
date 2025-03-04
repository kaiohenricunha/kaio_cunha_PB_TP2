#!/usr/bin/env python3
"""
Exercício 1.1: Download Assíncrono de URLs
Desenvolvido utilizando o editor de texto VI.
Objetivo: Utilizar asyncio e aiohttp para realizar downloads assíncronos de uma lista de URLs,
         variar o número de downloads simultâneos (controlados por um Semaphore) e medir o tempo
         total para completar as tarefas. Por fim, é gerado um gráfico que relaciona o número
         de downloads concorrentes x tempo de execução.
"""

import asyncio
import aiohttp
import time
import matplotlib.pyplot as plt

# Lista de URLs para download.
# Para efeito de teste, utilizo a mesma URL repetidamente.
# Em um cenário real, esta lista pode conter URLs diversas.
NUM_DOWNLOADS = 50
urls = ["http://example.com" for _ in range(NUM_DOWNLOADS)]

async def fetch(session: aiohttp.ClientSession, url: str, semaphore: asyncio.Semaphore) -> None:
    """Faz o download de uma URL utilizando a sessão assíncrona e respeitando o limite do semaphore."""
    async with semaphore:
        async with session.get(url) as response:
            # Lê o conteúdo da resposta (pode ser modificado conforme necessário)
            await response.text()

async def download_all(urls: list, concurrency: int) -> None:
    """
    Realiza o download de todas as URLs utilizando um número máximo de tarefas concorrentes (concurrency).
    
    Parâmetros:
      urls: Lista de URLs a serem baixadas.
      concurrency: Número máximo de downloads assíncronos simultâneos.
    """
    semaphore = asyncio.Semaphore(concurrency)
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch(session, url, semaphore)) for url in urls]
        await asyncio.gather(*tasks)

async def run_test(concurrency: int) -> float:
    """
    Executa o download de todas as URLs com um dado nível de concorrência e retorna o tempo de execução.
    
    Parâmetros:
      concurrency: Número máximo de tarefas concorrentes.
      
    Retorna:
      Tempo total de execução (em segundos).
    """
    start_time = time.time()
    await download_all(urls, concurrency)
    end_time = time.time()
    return end_time - start_time

async def main():
    # Definir diferentes níveis de concorrência para testar.
    # Apesar do exercício mencionar "threads", aqui consideramos o número de tarefas assíncronas simultâneas.
    concurrency_levels = [1, 5, 10, 20, 50, 100]
    times = []

    # Executa o teste para cada nível de concorrência.
    for concurrency in concurrency_levels:
        elapsed = await run_test(concurrency)
        print(f"Concorrência: {concurrency:3d} downloads -> Tempo: {elapsed:.2f} segundos")
        times.append(elapsed)

    # Gera o gráfico de desempenho: número de tarefas concorrentes x tempo de execução.
    plt.figure()
    plt.plot(concurrency_levels, times, marker="o")
    plt.title("Desempenho do Download Assíncrono")
    plt.xlabel("Número de downloads concorrentes")
    plt.ylabel("Tempo total de execução (s)")
    plt.grid(True)
    plt.savefig("grafico_desempenho.png")
    plt.show()

# Executa o programa principal utilizando asyncio.
if __name__ == "__main__":
    asyncio.run(main())

