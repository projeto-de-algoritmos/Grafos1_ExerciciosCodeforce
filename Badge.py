from collections import defaultdict
 
class Graph(object): 
    def __init__(self):
        self.adj = defaultdict(list)
 
    def adiciona_aresta(self, u, v): 
        self.adj[u].append(v)
 
def bfs(grafo, o, visited): 
    queue = []
    queue.append(o)
    visited[o] = True
    while queue: 
        m = queue.pop(0) 
        for neighbour in grafo.adj[m]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)
            else: 
                return neighbour
    return -1


def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    grafo = Graph()
    visited = []
    for i in range(n): 
        grafo.adiciona_aresta(i+1, numbers[i])
    for i in range(n):
        visited = [False] * (n+2)
        print(bfs(grafo, i+1, visited))
 
if __name__ == '__main__': 
    main()