import heapq
import networkx as nx

class ConjuntosDisjuntos:
    def __init__(self, elementos):
        self.pai = {e: e for e in elementos}
        self.tamanho = {e: 1 for e in elementos}

    def encontrar(self, x):
        if self.pai[x] != x:
            self.pai[x] = self.encontrar(self.pai[x])
        return self.pai[x]

    def unir(self, a, b):
        ra = self.encontrar(a)
        rb = self.encontrar(b)

        if ra == rb:
            return False

        if self.tamanho[ra] < self.tamanho[rb]:
            ra, rb = rb, ra

        self.pai[rb] = ra
        self.tamanho[ra] += self.tamanho[rb]
        return True


def mst_kruskal(grafo, peso='weight'):
    lista_arestas = []

    for u, v, dados in grafo.edges(data=True):
        w = dados.get(peso, 1.0)
        lista_arestas.append((w, u, v))

    lista_arestas.sort(key=lambda t: t[0])

    ds = ConjuntosDisjuntos(grafo.nodes)

    mst = nx.Graph()
    mst.add_nodes_from(grafo.nodes(data=True))

    custo_total = 0.0

    for w, u, v in lista_arestas:
        if ds.unir(u, v):
            mst.add_edge(u, v, weight=float(w))
            custo_total += w

        if mst.number_of_edges() == grafo.number_of_nodes() - 1:
            break

    return mst, custo_total


def mst_prim(grafo, inicio=None, peso='weight'):

    if grafo.number_of_nodes() == 0:
        return nx.Graph(), 0.0

    if inicio is None:
        inicio = next(iter(grafo.nodes))

    visitados = set()
    pais = {}
    chave = {n: float('inf') for n in grafo.nodes}
    chave[inicio] = 0.0

    heap = [(0.0, inicio, None)]
    custo_total = 0.0

    while heap and len(visitados) < grafo.number_of_nodes():
        peso_u, u, pai = heapq.heappop(heap)
        if u in visitados:
            continue

        visitados.add(u)
        pais[u] = pai

        if pai is not None:
            custo_total += peso_u

        for v in grafo.neighbors(u):
            if v in visitados:
                continue

            dados = grafo.get_edge_data(u, v, {})
            w = dados.get(peso, 1.0)

            if w < chave[v]:
                chave[v] = w
                heapq.heappush(heap, (float(w), v, u))

    arvore = nx.Graph()
    arvore.add_nodes_from(grafo.nodes(data=True))

    for v, u in pais.items():
        if u is None:
            continue

        w = grafo.get_edge_data(u, v, {}).get(peso, 1.0)
        arvore.add_edge(u, v, weight=float(w))

    return arvore, custo_total
