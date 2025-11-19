import time
import tracemalloc
from carregar_mapa import carregar_mapa
from criar_grafo import *
from criar_mst import mst_prim, mst_kruskal

# carregar dados
dados = carregar_mapa()

# criar grafo apenas 1 vez
grafo = criar_nos(dados)
grafo = criar_arestas_k_vizinhos(grafo, k=3)

# listas para armazenar
tempos_prim = []
custos_prim = []
memorias_prim = []

tempos_kruskal = []
custos_kruskal = []
memorias_kruskal = []

# repetir 10 vezes
for _ in range(10):

    # ======= PRIM =======
    tracemalloc.start()
    inicio = time.time()
    mst1, custo1 = mst_prim(grafo)
    fim = time.time()
    mem_atual, mem_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    tempos_prim.append(fim - inicio)
    custos_prim.append(custo1)
    memorias_prim.append(mem_pico / 1024)  # KB

    # ===== KRUSKAL =====
    tracemalloc.start()
    inicio = time.time()
    mst2, custo2 = mst_kruskal(grafo)
    fim = time.time()
    mem_atual, mem_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    tempos_kruskal.append(fim - inicio)
    custos_kruskal.append(custo2)
    memorias_kruskal.append(mem_pico / 1024)  # KB


print("\nRESULTADOS FINAIS:")
print("--------------------------------------")

print(f"Tempo médio Prim: {sum(tempos_prim)/10:.6f} s")
print(f"Custo médio Prim: {sum(custos_prim)/10:.2f}")
print(f"Memória média Prim: {sum(memorias_prim)/10:.2f} KB")

print("--------------------------------------")

print(f"Tempo médio Kruskal: {sum(tempos_kruskal)/10:.6f} s")
print(f"Custo médio Kruskal: {sum(custos_kruskal)/10:.2f}")
print(f"Memória média Kruskal: {sum(memorias_kruskal)/10:.2f} KB")

print("--------------------------------------")
