from collections import defaultdict

class Graph(object): 
    def __init__(self, N):
        self.N = N
        self.adj = defaultdict(set)

    def adiciona_aresta(self, u, v): 
        self.adj[u].add(v)
        self.adj[v].add(u)

    def printar(self):
        print(self.adj)


def mdc(a, b):
  while(b != 0):
    resto = a % b
    a = b
    b = resto
  
  return a

def caminho_minimo(grafo, o, f): 
    pass

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    o, f = map(int, input().split())

    for i in range(len(numbers)): 
        for j in range(i+1, len(numbers)): 
            if(mdc(numbers[i], numbers[j])!=1):
                grafo = Graph(n)
                grafo.adiciona_aresta(numbers[i], numbers[j])

    

if __name__ == '__main__': 
    main()
