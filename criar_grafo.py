import networkx as nx
from carregar_mapa import carregar_mapa
import math
import matplotlib.pyplot as plt

def criar_nos(geo_df):
  
    G = nx.Graph()

    for _, row in geo_df.iterrows():
        nome = row['EBAIRRNOME']
        x = row['x']
        y = row['y']

        # adiciona o nó ao grafo, com posição armazenada
        G.add_node(nome, pos=(x, y))

    return G


def criar_arestas_k_vizinhos(G, k=3):
    """
    Recebe um grafo com nós já criados e adiciona arestas
    conectando cada bairro aos k vizinhos mais próximos.
    """

    # lista com todos os nós
    nos = list(G.nodes(data=True))

    # para cada nó do grafo
    for i, (bairro1, dados1) in enumerate(nos):

        x1, y1 = dados1['pos']

        distancias = []

        # comparar com todos os outros bairros
        for j, (bairro2, dados2) in enumerate(nos):
            if bairro1 == bairro2:
                continue  # não calcula distância para ele mesmo

            x2, y2 = dados2['pos']

            # calcular distância
            d = math.dist((x1, y1), (x2, y2))

            # armazenar
            distancias.append((bairro2, d))

        # ordenar pelas menores distâncias
        distancias.sort(key=lambda t: t[1])

        # pegar somente os k vizinhos mais próximos
        vizinhos = distancias[:k]

        # criar arestas
        for bairro2, d in vizinhos:
            G.add_edge(bairro1, bairro2, weight=d)

    return G






if __name__ == "__main__":
    df = carregar_mapa()
    G = criar_nos(df)
    G = criar_arestas_k_vizinhos(G, k=3)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10)
    plt.show()
    print("Nós:", G.number_of_nodes())
    print("Arestas:", G.number_of_edges())

