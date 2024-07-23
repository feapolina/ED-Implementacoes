import time

# Preparando a leitura das instâncias
with open('instancias-num/num.10000.4.in', 'r') as arquivo:
    linhas = arquivo.readlines()

# Inicializando vetor vazio e atribuindo ao array já "cortado"
array = []
for linha in linhas:
    # Iterando, removendo espaços em branco e convertendo para inteiro.
    valor = int(linha.strip())
    array.append(valor)


def selectionSort(array):
    for indice in range(0, len(array)):
        minimo = indice

        for elementoDireita in range(indice + 1, len(array)):
            if array[elementoDireita] < array [minimo]:
                minimo = elementoDireita
        
        array[indice], array[minimo] = array[minimo], array[indice]

def tempoExecucaoAlgoritmo(algoritmoOrdenacao, array):
    inicio = time.time()
    print(algoritmoOrdenacao(array))
    fim = time.time()
    tempo_decorrido = fim - inicio
    print("Execução do Selection Sort em: {:.2f} segundos".format(tempo_decorrido))

tempoExecucaoAlgoritmo(selectionSort, array)