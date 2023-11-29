class Grafo:

    def __init__(self,vertices) -> None:
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]
    
    def adicionar_aresta(self,vertice_inicial,vertice_final):
        # pensando em grafo direcionado
        self.grafo[vertice_inicial].append(vertice_final)

        #se o grafo for não direcionado
        self.grafo[vertice_final].append(vertice_inicial)

    def print_grafo(self):
        for i in range(self.vertices):
            print(f'{i}:',end='  ')
            for j in self.grafo[i]:
                print(f'{j}  ->',end='  ')
            print('')

g = Grafo(4)
g.adicionar_aresta(0,1)
g.adicionar_aresta(0,2)
g.adicionar_aresta(1,2)
g.print_grafo()
