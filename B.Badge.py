from collections import defaultdict

visited = []
class Graph(object): 
    def __init__(self, N):
        self.N = N
        self.adj = defaultdict(set)

    def adiciona_aresta(self, u, v): 
        self.adj[u].add(v)


def dfs(grafo, o): 
    if o not in visited: 
        visited.append(o)
        for neighbour in grafo.adj[o]:
            dfs(grafo, neighbour)
    else: 
        print(o)

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    grafo = Graph(n)
    for i in range(len(numbers)): 
        grafo.adiciona_aresta(i+1, numbers[i])
    for i in range(n):
        visited.clear()
        dfs(grafo, i+1)
    

if __name__ == '__main__': 
    main()
