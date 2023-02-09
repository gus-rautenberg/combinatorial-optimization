import numpy as np
import random
import math

i = 0;
k = 1;


# Lendo o arquivo e usando sua primeira linha para saber o tamanho da matriz

#filename = input("Nome do arquivo: ")

arq = open('Entrada 10.txt', 'r')

Primeiralinha = arq.readline(2)
arq.close()
Numeromatriz = int(Primeiralinha)
auxM = np.zeros((Numeromatriz+1, Numeromatriz))

#=============================================

arq = open('Entrada 10.txt', 'r')

# Transformando os dados do arquivo em uma matriz

for linha in arq:
  #print(linha)
  auxLinha = linha
  Lista = auxLinha.split()
  nums = [int(s) for s in Lista]
  auxM[i,:] = nums[:]
  i= i+1
  
auxM = np.delete(auxM, (0), 0)

#============================================

#ale = random.randrange(0, Numeromatriz)

# (Não pronto) Gerando a primeira solução
listaCidades = np.zeros(Numeromatriz)
listaResultados = np.zeros(Numeromatriz)
piorInicial = Numeromatriz
piorInicialLoc = np.zeros((1,2))
for t in range(Numeromatriz):
    for j in range(Numeromatriz):
        teste = auxM[t][j]
        if(teste < piorInicial and teste != 0):
            piorInicial = teste
            piorInicialLoc[0][0] = t
            piorInicialLoc[0][1] = j
            listaResultados[0] = piorInicial
            
            
for k in range(10):
    piorInicial = Numeromatriz
    auxCidade = piorInicialLoc[0][0]
    auxProxCidade = piorInicialLoc[0][1]
    proxCidade = int(auxProxCidade)
    listaCidades[k] = auxCidade
    for t in range(Numeromatriz):
        jorge = auxM[proxCidade][t]
        for v in range(Numeromatriz):
            if(t != listaCidades[v]):
                if(jorge < piorInicial and jorge != 0):
                    piorInicial = jorge
                    piorInicialLoc[0][0] = proxCidade
                    piorInicialLoc[0][1] = t
                    listaResultados = np.append(k+1, t)
            
            
    


            
