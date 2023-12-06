class Grafo:
    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = []
        for i in range(self.vertices):
            self.grafo.append([0]*self.vertices) # Cria uma matriz (uma lista de listas)
    
    def adicionar_aresta(self,vertice_inicial,vertice_final):
        # Estou pensando em grafos não direcionados
        self.grafo[vertice_inicial][vertice_final] += 1
        if vertice_inicial != vertice_final:   
            self.grafo[vertice_final][vertice_inicial] += 1
    
    def print_grafo(self):
        for i in self.grafo:
            print(i)
    
    def acessibilidade(self,vertice_inicial,vertice_final):
        if self.grafo[vertice_inicial][vertice_final] == 0:
            print(f'não tem aresta entre os vertices {vertice_inicial} e {vertice_final}')
        else:
            print(f'Existe {self.grafo[vertice_inicial][vertice_final]} arestas entre os vertices {vertice_inicial} e {vertice_final}')
    
    def is_Eulerian(self):
        contador = 0
        for linha in range(self.vertices):
            grau = 0
            for coluna in range(self.vertices):
                if linha == coluna:
                    grau += self.grafo[linha][coluna] * 2
                else:
                    grau += self.grafo[linha][coluna]
            if grau % 2 != 0:
                contador += 1
        if contador == 0:
            print('É um grafo Euleriano')
        elif contador == 2:
            print('É um grafo SemiEuleriano')
        else:
            print('O grafo  nãe é Euleriano e nem  semieulariano')

    

# Teste para vê se está funcionando
g = Grafo(5)

g.adicionar_aresta(vertice_inicial=1,vertice_final=2)
g.adicionar_aresta(vertice_inicial=3,vertice_final=4)
g.adicionar_aresta(vertice_inicial=2,vertice_final=3)
g.adicionar_aresta(vertice_inicial=1,vertice_final=4)
g.adicionar_aresta(vertice_inicial=0,vertice_final=0)

g.acessibilidade(1,2)
g.acessibilidade(4,1)

g.is_Eulerian()

g.print_grafo()
