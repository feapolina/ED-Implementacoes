# Aluno: Felipe Cavalcanti Apolinário

tamMax = 10;
tamAtual = 0;
dados = [0] * tamMax
inicio = 0
final = -1

def vazia():
    return tamAtual == 0 

def cheia():
    return tamAtual == tamMax

def consultaInicio():
    if vazia():
        return "A fila está vazia."
    return dados[inicio]

def insere(valor):
    global final, tamAtual
    if cheia():
        return "A fila está cheia. Não é possível inserir."
    
    final = (final + 1) % tamMax
    dados[final] = valor
    tamAtual += 1
    return True

def remove():
    global inicio, tamAtual
    if vazia():
        return "Não há o que remover."
    
    dados[inicio] = 0
    inicio = (inicio + 1) % tamMax
    tamAtual -= 1
    

def mostraVetor():
    elementos_fila = []
    i = inicio
    for _ in range(tamAtual):
        elementos_fila.append(dados[i])
        i = (i + 1) % tamMax
    print(elementos_fila)

insere(3)
insere(4)
insere(5)
insere(7)

mostraVetor()
print("A lista está vazia?", vazia())
print("A lista está cheia?", cheia())
print("Elemento do inicio da fila:", consultaInicio())
print("\n---- removendo... ----")
remove()
mostraVetor()
print("\n---- removendo... ----")
remove()
mostraVetor()
print("\n---- consultando novo inicio... ----")
print("Elemento do inicio da fila:", consultaInicio())