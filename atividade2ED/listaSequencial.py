#Definindo os limites do vetor
tamMax = 10;
tamAtual = 5;
dados = [0] * tamMax 
dados[:tamAtual] = [2, 3, 1, 5, 4]

def vazia():
    if tamAtual == 0:
        return True
    else :
        return False

def cheia():
    if tamAtual == tamMax:
        return True
    else:
        return False

def tamanhoLista():
    return tamAtual

def retornaElementoNaPosicao(posicaoLista):
    if (posicaoLista > tamAtual) or (posicaoLista < 0):
        return "Não é possível buscar este valor. Está fora dos limites."
    else:
        dado = dados[posicaoLista - 1]
        return dado;
    
def modificaElementoNaPosicao(posicaoLista, numero):
    if (posicaoLista > tamAtual) or (posicaoLista <= 0):
        return "Não é possível alterar este elemento pois está fora dos limites."
    else: 
        numeroAnterior = dados[posicaoLista - 1]
        dados[posicaoLista - 1 ] = numero
        print(dados)
        return f"Elemento alterado de {numeroAnterior} para {numero}"
    
def insereElementoNaPosicao(posicaoLista, numero):
    global tamAtual
    if (cheia() or (posicaoLista > tamAtual + 1) or (posicaoLista <= 0)):
        return "Não é possível adicionar um elemento na posição indicada."
    
    for i in range(tamAtual, posicaoLista - 1, -1):
        dados[i] = dados[i - 1]
    
    dados[posicaoLista - 1] = numero;
    print(f"Valor {numero} adicionado na posição {posicaoLista}")
    print(dados)
    tamAtual += 1
    return True

def removeElementoNaPosicao(posicaoLista):
    global tamAtual
    if (vazia() or (posicaoLista > tamAtual + 1) or (posicaoLista < 1)):
        return "Não é possível remover um elemento na posição indicada."

    dado = dados[posicaoLista - 1] = 0
    for i in range(posicaoLista - 1, tamAtual - 1):
        dados[i] = dados[i+1]
    
    tamAtual-= 1
    return dado

print(dados)
print(vazia())
print(cheia())
print(tamanhoLista())
print(retornaElementoNaPosicao(4))
print(modificaElementoNaPosicao(3, 5))
print(insereElementoNaPosicao(3, 1))
print(removeElementoNaPosicao(6))
print(dados[:tamAtual])
