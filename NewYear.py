from collections import defaultdict
 
class Graph(object): 
    def __init__(self):
        self.adj = defaultdict(list)
 
    def adiciona_aresta(self, u, v): 
        self.adj[u].append(v)
 
def bfs(graph, o, t): 
    if(t == o): 
        return True
    visited = set([o])
    queue = [o]
    while queue:
        m = queue.pop()
        for node in graph.adj[m]:
            if node not in visited:
                if node == t:
                    return True
                visited.add(node)
                queue.append(node)
    return False


def main():
    n, t = map(int, input().split())
    numbers = list(map(int, input().split()))
    graph = Graph()
    for i in range(n-1):
        graph.adiciona_aresta(i+1, numbers[i]+(i+1))
        
    print("YES" if bfs(graph, 1, t) else "NO")

 
if __name__ == '__main__': 
    main()