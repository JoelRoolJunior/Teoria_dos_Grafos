class Grafo:

    def __init__(self,vertices) -> None:
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]
    
    def adicionar_aresta(self,vertice_inicial,vertice_final,peso):
        # pensando em grafo direcionado
        self.grafo[vertice_inicial].append([vertice_final,peso])

        #se o grafo for não direcionado
        self.grafo[vertice_final].append([vertice_inicial,peso])

    def print_grafo(self):
        for i in range(self.vertices):
            print(f'{i}:',end='  ')
            for j in self.grafo[i]:
                print(f'{j}  ->',end='  ')
            print('')

g = Grafo(4)
g.adicionar_aresta(0,1,20)
g.adicionar_aresta(0,2,15)
g.adicionar_aresta(1,2,5)
g.print_grafo()
