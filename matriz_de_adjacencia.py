class Grafo:
    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = []
        for i in range(self.vertices):
            self.grafo.append([0]*self.vertices) # Cria uma matriz (uma lista de listas)
    
    def adicionar_aresta(self,vertice_inicial,vertice_final):
        self.grafo[vertice_inicial][vertice_final] = 1
        self.grafo[vertice_final][vertice_inicial] = 1
    
    def print_grafo(self):
        for i in self.grafo:
            print(i)

# Teste para vê se está funcionando
g = Grafo(3)
g.adicionar_aresta(vertice_inicial=0,vertice_final=1)
g.adicionar_aresta(vertice_inicial=0,vertice_final=2)
g.adicionar_aresta(vertice_inicial=0,vertice_final=3)
g.adicionar_aresta(vertice_inicial=0,vertice_final=4)
g.print_grafo()
