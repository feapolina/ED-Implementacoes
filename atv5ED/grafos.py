# Aluno: Felipe Cavalcanti Apolinario

class GrafoBase:
    def __init__(self, nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            self.num_vertices = int(arquivo.readline())
            self.dados = [list(map(int, linha.split())) for linha in arquivo]

class GrafoMatriz(GrafoBase):
    def __init__(self, nome_arquivo):
        super().__init__(nome_arquivo)
        self.matriz_adj = self.dados  # Apenas copia os dados para a matriz de adjacência

    def imprimir_matriz(self):
        for linha in self.matriz_adj:
            print(linha)

class GrafoLista(GrafoBase):
    def __init__(self, nome_arquivo):
        super().__init__(nome_arquivo)
        self.lista_adj = [[] for _ in range(self.num_vertices)]
        for i in range(self.num_vertices):
            for j, peso in enumerate(self.dados[i]):
                if peso > 0:
                    self.lista_adj[i].append(j)  # Adiciona apenas os vértices adjacentes

    def imprimir_lista(self):
        for vertice, adjacentes in enumerate(self.lista_adj):
            print(f'{vertice}: {adjacentes}')

    def bfs_recursiva(self, nivel_atual, visitados, predecessores):
        if not nivel_atual:
            return

        proximo_nivel = []
        for vertice_atual in nivel_atual:
            for vizinho in self.lista_adj[vertice_atual]:
                if not visitados[vizinho]:
                    visitados[vizinho] = True
                    predecessores[vizinho] = vertice_atual
                    proximo_nivel.append(vizinho)
        self.bfs_recursiva(proximo_nivel, visitados, predecessores)

    def caminho_bfs(self, s, t):
        visitados = [False] * len(self.lista_adj)
        predecessores = [-1] * len(self.lista_adj)
        visitados[s] = True
        self.bfs_recursiva([s], visitados, predecessores)

        if not visitados[t]:
            print(f"Não há caminho entre os vértices {s} e {t}.")
        else:
            caminho = []
            atual = t
            while atual != -1:
                caminho.append(atual)
                atual = predecessores[atual]
            caminho.reverse()
            print(f"Caminho entre os vértices {s} e {t}: {' -> '.join(map(str, caminho))}")

    def dfs_iterativa(self, inicio):
        visitados = [False] * len(self.lista_adj)
        pilha = [inicio]

        while pilha:
            vertice_atual = pilha.pop()
            if not visitados[vertice_atual]:
                print(vertice_atual, end=" ")
                visitados[vertice_atual] = True
                for vizinho in reversed(self.lista_adj[vertice_atual]):
                    if not visitados[vizinho]:
                        pilha.append(vizinho)

    def caminho_dfs(self, s, t):
        visitados = [False] * len(self.lista_adj)
        predecessores = [-1] * len(self.lista_adj)
        pilha = [s]

        while pilha:
            vertice_atual = pilha.pop()
            if not visitados[vertice_atual]:
                visitados[vertice_atual] = True
                if vertice_atual == t:
                    break
                for vizinho in reversed(self.lista_adj[vertice_atual]):
                    if not visitados[vizinho]:
                        pilha.append(vizinho)
                        predecessores[vizinho] = vertice_atual

        if not visitados[t]:
            print(f"Não há caminho entre os vértices {s} e {t}.")
        else:
            caminho = []
            atual = t
            while atual != -1:
                caminho.append(atual)
                atual = predecessores[atual]
            caminho.reverse()
            print(f"Caminho entre os vértices {s} e {t}: {' -> '.join(map(str, caminho))}")

# Exemplo de uso
grafo_matriz = GrafoMatriz('instancias-grafo/pcv4.txt')
print("\nMatriz de Adjacência:")
grafo_matriz.imprimir_matriz()

grafo_lista = GrafoLista('instancias-grafo/pcv4.txt')
print("\nLista de Adjacência:")
grafo_lista.imprimir_lista()

print("\nCaminho BFS entre 0 e 3:")
grafo_lista.caminho_bfs(0, 3)

print("\nBusca em Profundidade (DFS) a partir do vértice 0:")
grafo_lista.dfs_iterativa(0)
print()

print("\nCaminho DFS entre 0 e 3:")
grafo_lista.caminho_dfs(0, 3)
