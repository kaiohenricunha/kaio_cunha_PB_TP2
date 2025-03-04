#!/usr/bin/env python3
"""
Exercício 1.3: Processamento de Imagens Assíncrono

Objetivo:
- Ler várias imagens de uma pasta de entrada.
- Aplicar um filtro (neste exemplo, BLUR) usando a biblioteca Pillow.
- Processar as imagens de forma assíncrona utilizando asyncio e um ThreadPoolExecutor.
- Salvar as imagens filtradas em uma pasta de saída.
- Variar o número de threads (max_workers) e medir o tempo total de processamento.
- Gerar um gráfico comparando o número de threads x tempo de processamento.

Instruções:
1. Crie uma pasta chamada "input_images" com imagens JPEG para testar.
2. As imagens processadas serão salvas na pasta "output_images".
3. Execute o script e analise o gráfico gerado.
"""

import os
import glob
import time
import asyncio
import concurrent.futures
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

def process_image(image_path, output_dir):
    """
    Abre uma imagem, aplica o filtro BLUR, converte para RGB (se necessário)
    e salva a imagem processada na pasta de saída.
    """
    try:
        img = Image.open(image_path)
        filtered_img = img.filter(ImageFilter.BLUR)
        # Converte para RGB se a imagem tiver canal alfa
        if filtered_img.mode != "RGB":
            filtered_img = filtered_img.convert("RGB")
        base_name = os.path.basename(image_path)
        output_path = os.path.join(output_dir, base_name)
        filtered_img.save(output_path)
    except Exception as e:
        print(f"Erro ao processar {image_path}: {e}")

async def process_images_concurrently(image_paths, output_dir, max_workers):
    """
    Processa as imagens de forma assíncrona utilizando run_in_executor.
    
    Parâmetros:
      image_paths: Lista de caminhos das imagens.
      output_dir: Diretório para salvar as imagens processadas.
      max_workers: Número de threads a serem utilizadas no pool.
    """
    loop = asyncio.get_running_loop()
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        tasks = [
            loop.run_in_executor(executor, process_image, image_path, output_dir)
            for image_path in image_paths
        ]
        await asyncio.gather(*tasks)

async def main():
    # Diretórios de entrada e saída
    input_dir = "input_images"
    output_dir = "output_images"
    os.makedirs(output_dir, exist_ok=True)
    
    # Lista todas as imagens JPEG na pasta de entrada
    image_paths = glob.glob(os.path.join(input_dir, "*.jpg"))
    if not image_paths:
        print("Nenhuma imagem JPEG encontrada na pasta 'input_images'.")
        return

    # Variação do número de threads (workers) para testes
    thread_counts = [1, 2, 4, 8, 16]
    times_list = []
    
    for threads in thread_counts:
        # Limpa a pasta de saída antes de cada teste
        for file in os.listdir(output_dir):
            os.remove(os.path.join(output_dir, file))
        
        start_time = time.time()
        await process_images_concurrently(image_paths, output_dir, threads)
        elapsed = time.time() - start_time
        print(f"Threads: {threads:2d} -> Tempo: {elapsed:.2f} s")
        times_list.append(elapsed)
    
    # Gera o gráfico de desempenho
    plt.figure()
    plt.plot(thread_counts, times_list, marker="o")
    plt.title("Processamento de Imagens: Número de Threads x Tempo")
    plt.xlabel("Número de Threads")
    plt.ylabel("Tempo de Processamento (s)")
    plt.grid(True)
    plt.savefig("grafico_imagens.png")
    plt.show()

if __name__ == "__main__":
    asyncio.run(main())
