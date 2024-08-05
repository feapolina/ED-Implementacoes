# Aluno: Felipe Cavalcanti Apolinario (20220070841)
# Essa foi a minha terceira interação com python então muita coisa deve ter sido feita de um jeito meio ruim...
# Espero que tenha atingido o objetivo da atividade. Em comparação com a última atividade, essa foi bem mais complexa, na minha opinião

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def adicionar(self, valor, posicao=None):
        novo_no = No(valor)

        # Adicionar no final da lista
        if posicao is None:  
            if self.primeiro is None:
                self.primeiro = novo_no
            else:
                atual = self.primeiro
                while atual.proximo is not None:
                    atual = atual.proximo
                atual.proximo = novo_no

        # Adicionar na posição específica
        else:  
            # Adicionar no início
            if posicao == 0:  
                novo_no.proximo = self.primeiro
                self.primeiro = novo_no
            else:
                atual = self.primeiro
                contador = 0
                while atual is not None and contador < posicao - 1:
                    atual = atual.proximo
                    contador += 1
                if atual is None:
                    raise IndexError("Posição inválida")
                novo_no.proximo = atual.proximo
                atual.proximo = novo_no

    def remover(self, posicao):
        if posicao == 0:
            self.primeiro = self.primeiro.proximo
            return
        atual = self.primeiro
        anterior = None
        contador = 0
        while atual is not None:
            if contador == posicao:
                anterior.proximo = atual.proximo
                return
            anterior = atual
            atual = atual.proximo
            contador += 1
        raise IndexError("Posição inválida")

    def verifica_vazio(self):
        return self.primeiro is None

    def obtem_tamanho_lista(self):
        contador = 0
        atual = self.primeiro
        while atual is not None:
            contador += 1
            atual = atual.proximo
        return contador
    
    def obter_elemento(self, posicao):
        atual = self.primeiro 
        contador = 0
        while atual is not None:
            if contador == posicao:
                return atual.valor
            contador += 1
            atual = atual.proximo
        raise IndexError("Posição inválida")
    
    def modifica_elemento(self, posicao, novo_elemento):
        atual = self.primeiro
        contador = 0
        while atual is not None:
            if contador == posicao:
                atual.valor = novo_elemento
                return
            contador += 1
            atual = atual.proximo
        raise IndexError("Posição inválida")

    def imprimir_elementos_lista(self):
        if self.verifica_vazio():
            print("Lista vazia")
        else:
            elementos = []
            atual = self.primeiro
            while atual is not None:
                elementos.append(atual.valor)
                atual = atual.proximo
            print(elementos)

def testes():
    lista = ListaEncadeada()

    # Adicionar elementos no final
    lista.adicionar(35)
    lista.adicionar(10)
    lista.adicionar(20)
    lista.adicionar(30)
    print("Mostrando elementos da lista:")
    # Os elementos estão sendo mostrados como array. Bem como as posições especificadas estao sendo interpretadas como array. Gosto da visualização no estilo de array.
    lista.imprimir_elementos_lista()

    # Obter tamanho da lista
    print("Tamanho da lista: ", lista.obtem_tamanho_lista())

    # Verificar se a lista está vazia
    print("A lista está vazia?", lista.verifica_vazio())

    # Obter elemento em uma posição
    print("Elemento na posição 2: ", lista.obter_elemento(2))
    print("Elemento na posição 3: ", lista.obter_elemento(3))

    # Modificar elemento em uma posição
    print("Modificando o elemento na posicao 2 para 314")
    lista.modifica_elemento(2, 314)
    lista.imprimir_elementos_lista()

    # Remover elemento em uma posição
    print("Removendo o elemento na posicao 3")
    lista.remover(3)
    lista.imprimir_elementos_lista()

    # Adicionar na última posição
    print("Adicionando 50 na 2 posição")
    lista.adicionar(50, 2)
    lista.imprimir_elementos_lista()

if __name__ == "__main__":
    testes()
 