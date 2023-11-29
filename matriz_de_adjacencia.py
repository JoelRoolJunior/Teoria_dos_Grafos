class Grafo:
    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = []
        for i in range(self.vertices):
            self.grafo.append([0]*self.vertices) # Cria uma matriz (uma lista de listas)
    
    def adicionar_aresta(self,vertice_inicial,vertice_final,peso):
        self.grafo[vertice_inicial][vertice_final] = peso
        self.grafo[vertice_final][vertice_inicial] = peso
    
    def print_grafo(self):
        for i in self.grafo:
            print(i)

# Teste para vê se está funcionando
g = Grafo(5)
g.adicionar_aresta(vertice_inicial=0,vertice_final=1,peso=5)
g.adicionar_aresta(vertice_inicial=0,vertice_final=2,peso=10)
g.adicionar_aresta(vertice_inicial=0,vertice_final=3,peso=15)
g.adicionar_aresta(vertice_inicial=0,vertice_final=4,peso=20)
g.print_grafo()
