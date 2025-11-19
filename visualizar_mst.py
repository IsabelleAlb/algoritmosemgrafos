from carregar_mapa import carregar_mapa
from criar_grafo import *
from criar_mst import mst_prim, mst_kruskal
import networkx as nx
import matplotlib.pyplot as plt

# carregar bairros
df = carregar_mapa()

# criar grafo completo
G = criar_nos(df)
G = criar_arestas_k_vizinhos(G)

# gerar MST (Prim ou Kruskal)
mst, custo_total = mst_kruskal(G)
# mst, custo_total = mst_prim(G)

# criar posições dos bairros
pos = {}
for n in mst.nodes():
    x = df.loc[df["EBAIRRNOME"] == n, "x"].values[0]
    y = df.loc[df["EBAIRRNOME"] == n, "y"].values[0]
    pos[n] = (x, y)

# desenhar nós e arestas
nx.draw(mst, pos, with_labels=True, node_size=50, font_size=6)


pesos_formatados = {}
for (u, v, d) in mst.edges(data=True):
    peso = d["weight"]                    
    peso_formatado = f"{(peso/1000):.2f} km"    
    pesos_formatados[(u, v)] = peso_formatado

# desenhar pesos no grafo
nx.draw_networkx_edge_labels(
    mst,
    pos,
    edge_labels=pesos_formatados,
    font_size=8
)

plt.show()

print(f"Custo total da MST: {custo_total:.2f} km")
