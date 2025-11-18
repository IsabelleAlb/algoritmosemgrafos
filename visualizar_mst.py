from carregar_mapa import carregar_mapa
from criar_grafo import *
from criar_mst import mst_prim, mst_kruskal
import networkx as nx
import matplotlib.pyplot as plt
import time

# carregar bairros
df = carregar_mapa()

# criar grafo completo
G = criar_nos(df)
G = criar_arestas_k_vizinhos(G)

# gerar MST
start = time.time()
mst, custo_total = mst_kruskal(G) #mst_prim(G)
end = time.time()
tempo_prim = end - start

# criar posições dos bairros para o desenho
pos = {}
for n in mst.nodes():
    x = df.loc[df["EBAIRRNOME"] == n, "x"].values[0]
    y = df.loc[df["EBAIRRNOME"] == n, "y"].values[0]
    pos[n] = (x, y)

# desenhar nós e arestas
nx.draw(mst, pos, with_labels=True, node_size=50, font_size=6)

# desenhar pesos das arestas
nx.draw_networkx_edge_labels(
    mst,
    pos,
    edge_labels=nx.get_edge_attributes(mst, "weight"),
    font_size=5
)

plt.show()

print(f"Tempo de execução do Algoritmo: {tempo_prim:.6f} segundos")
print(f"Custo total da MST: {custo_total:.2f}")
