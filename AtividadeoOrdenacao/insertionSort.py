import time

with open('instancias-num/num.10000.4.in', 'r') as arquivo:
    linhas = arquivo.readlines()


array = []

for linha in linhas:
    valor = int(linha.strip())
    array.append(valor)

def insertionSort(array):
    for indice in range(1, len(array)):
        valorAtual = array[indice]
        j = indice - 1

        while j >= 0 and array[j] > valorAtual:
            array[j + 1] = array[j]
            j -= 1
        
        array[j + 1] = valorAtual 

def tempoExecucaoAlgoritmo(algoritmoOrdenacao, array):
    inicio = time.time()
    print(algoritmoOrdenacao(array))
    fim = time.time()
    tempo_decorrido = fim - inicio
    print("Execução do Insertion Sort em : {:.2f} segundos".format(tempo_decorrido))

tempoExecucaoAlgoritmo(insertionSort, array)