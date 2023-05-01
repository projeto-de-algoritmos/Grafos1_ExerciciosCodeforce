from collections import defaultdict

dist = []
pa = []
visited = [] 
ordem = []
class Graph(object): 
    def __init__(self, N):
        self.N = N
        self.adj = defaultdict(set)

    def adiciona_aresta(self, u, v): 
        self.adj[u].add(v)
        self.adj[v].add(u)

def mdc(a, b):
  while(b != 0):
    resto = a % b
    a = b
    b = resto
  
  return a

def path(grafo, o, x):
    if(x==o): 
        return
    else: 
        path(grafo, o, visited[x])
        print(visited[x])

def cheap_path(grafo, o, n): 
    for i in range(n+1): 
        dist.append(4294967295)
    for i in range(n+1): 
        visited.append(0)

    dist[o] = 1
    queue = []     
    visited.append(o)
    queue.append(o)

    while queue: 
        m = queue.pop(0) 
        for neighbour in grafo.adj[m]:
            if visited[neighbour] == 0:
                if (dist[neighbour] > dist[m] + 1):
                    dist[neighbour] = dist[m] + 1
                    visited[neighbour] = m
                queue.append(neighbour)

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    o, f = map(int, input().split())
    ordem.append(f)
    grafo = {}
    grafo = Graph(n)
    for i in range(n): 
        for j in range(i+1, n):
            if(mdc(numbers[i], numbers[j])!=1):
                grafo.adiciona_aresta(i+1, j+1)

    cheap_path(grafo, o, n)
    if(dist[f]==4294967295): 
        print(-1)
    else: 
        print(dist[f])
        path(grafo, o, f)
        print(f)
    

if __name__ == '__main__': 
    main()
