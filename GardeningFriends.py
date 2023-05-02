from collections import deque, defaultdict

class Graph(object): 
    def __init__(self, N):
        self.N = N
        self.adj = defaultdict(list)

    def adiciona_aresta(self, u, v): 
        self.adj[u].append(v)
        self.adj[v].append(u)

def lucro_maximo(grafo, n, k, c):
    lucro_maximo = 0
    distancias_raiz = [0] * (n + 1)
    bfs(grafo, 1, distancias_raiz)

    for i in range(1, n+1):
        distancias = [0] * (n + 1)
        bfs(grafo, i, distancias)

        lucro = max(distancias) * k - distancias_raiz[i] * c

        if lucro > lucro_maximo:
            lucro_maximo = lucro

    return lucro_maximo

def bfs(grafo, no, distancias):
    visitados = [False] * (grafo.N + 1)
    fila = deque()
    fila.append(no)
    visitados[no] = True

    while fila:
        u = fila.popleft()
        for vizinho in grafo.adj[u]:
            if not visitados[vizinho]:
                visitados[vizinho] = True
                distancias[vizinho] = distancias[u] + 1
                fila.append(vizinho)

def main():
    t = int(input())
    for i in range(t):
        n, k, c = map(int, input().split())
        G = Graph(n+1)

        for j in range(n-1):
            u, v = map(int, input().split())
            G.adiciona_aresta(u, v)

        print(lucro_maximo(G, n, k, c))

if __name__ == '__main__': 
    main()
