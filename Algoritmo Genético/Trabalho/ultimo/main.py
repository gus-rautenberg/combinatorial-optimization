# Desenvolver uma solução de Otimização Combinatória
# com abordagem de um Algoritmo Genético
# Codificação: Binária      Seleção: Roleta
# Cruzamento: Dois Pontos   Mutação: Binária
# Elitismo: 1 indivíduo por Geração

# Função de Otimização: 𝑍 = −(𝑥² + y²) +4
# Restrições:    x ∈ [-10, 10] && y ∈ [-10, 10]

import numpy
import random
from Individual import Individual
from functions import *
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d



cromossomos = 30
pC = 0.75
pM = 0.025
pop_size = 100
contGen = 0
fitSum = 0
generations = 50


# Creating 3D figure
fig = plt.figure(figsize=(10, 10))
ax = plt.axes(projection='3d')


# nomenclaturas: final X é o cromossomo X, Y é o cromossomo Y
# ind: individuo passageiro
# sinal: sinal do numero
# inteira: parte inteira do numero
# decimal: parte decimal do numero
# real: numero em si
# fit: fit do numero na função
# novageração: aux para geração

indX = numpy.zeros(cromossomos)
indY = numpy.zeros(cromossomos)



#individuo = numpy.zeros(pop_size)

sinalX = numpy.zeros(pop_size)
sinalY = numpy.zeros(pop_size)

inteiraX = numpy.zeros(pop_size)
inteiraY = numpy.zeros(pop_size)

realX = numpy.zeros(pop_size)
realY = numpy.zeros(pop_size)

decimalX = numpy.zeros(pop_size)
decimalY = numpy.zeros(pop_size)

fit = numpy.zeros(pop_size)

newGenX = numpy.zeros((pop_size, cromossomos))
newGenY = numpy.zeros((pop_size, cromossomos))

probInd = numpy.zeros(pop_size)  # Probabilidades para calcular a roleta
probtotal = numpy.zeros(pop_size)  # Probabilidades para calcular a roleta

chad = 0  # indice do melhor indivíduo

# def getfitSum():
#     fitSum = sum([indFit.getFitness() for ind in self.population])
#     return self.fitSum


pop = numpy.zeros((pop_size, cromossomos))
initPop(pop, pop_size, cromossomos)

pop2 = numpy.zeros((pop_size, cromossomos))
initPop(pop2, pop_size, cromossomos)

newPopX = numpy.zeros((pop_size, cromossomos))
newPopY = numpy.zeros((pop_size, cromossomos))

while (contGen <= generations):
    newIndX = 0
    newIndY = 0
    
    
    while (newIndX <= (pop_size-1)):
        
        
        fitSum = 0
        #print(pop)
        #print('-----')
        #print(pop2)
        
        
        for i in range(pop_size):
            indX[:] = pop[i, :]
            indY[:] = pop2[i, :]

            aux = [int(i) for i in indX]
            aux2 = [int(i) for i in indY]

            sinalX[i] = indX[0]
            sinalY[i] = indY[0]

            inteiraX[i] = convert(aux[1:5])
            inteiraX[i] = binaryTodecimal(inteiraX[i])

            inteiraY[i] = convert(aux2[1:5])
            inteiraY[i] = binaryTodecimal(inteiraY[i])

            decimalX[i] = convert(aux[6:30])
            decimalX[i] = binaryTodecimal(decimalX[i])

            decimalY[i] = convert(aux2[6:30])
            decimalY[i] = binaryTodecimal(decimalY[i])

            intinteiraX = [int(i) for i in inteiraX]
            intdecimalX = [int(i) for i in decimalX]

            intinteiraY = [int(i) for i in inteiraY]
            intdecimalY = [int(i) for i in decimalY]

        for r in range(pop_size):

            aux = [int(r) for r in indX]
            aux2 = [int(r) for r in indY]

            digits = 0
            base = 10
            # print(intinteira[r])
            # print(intdecimal[r])
            realX[r] = numConcat(intinteiraX[r], intdecimalX[r])
            # print(realX[r])
            # intreal=[int(r) for r in real]
            if (intinteiraX[r] >= 10):
                realX[r] = 10

            if (intinteiraX[r] < 10 and intinteiraX[r] > 0):
                # print(realX[r])
                digits = len(str(realX[r]))
                realX[r] = realX[r]/(base**(digits-3))
                # print("-----------------------------=")
                # print(realX[r])

            if (intinteiraX[r] == 0):
                digits = len(str(realX[r]))
                realX[r] = realX[r]/(base**(digits-2))

            digits2 = 0
            base2 = 10
            realY[r] = numConcat(intinteiraY[r], intdecimalY[r])
            if (intinteiraY[r] >= 10):
                realY[r] = 10

            if (intinteiraY[r] == 0):
                digits2 = len(str(realY[r]))
                realY[r] = realY[r]/(base2**(digits2-2))

            if (intinteiraY[r] < 10 and intinteiraY[r] > 0):
                digits2 = len(str(realY[r]))
                realY[r] = realY[r]/(base2**(digits2-3))

            if (sinalX[r] == 1):
                realX[r] = realX[r]*-1

            if (sinalY[r] == 1):
                realY[r] = realY[r]*-1

        for r in range(pop_size):
            indX[:] = pop[r, :]
            indY[:] = pop2[r, :]

            if (sinalX[r] == 0 and inteiraX[r] >= 10):
                indX[:] = zeroToCrom(indX, cromossomos)
                inteiraX[r] = 10

            if (sinalX[r] == 1 and inteiraX[r] >= 10):
                indX[:] = oneToCrom(indX, cromossomos)
                inteiraX[r] = 10

            if (sinalY[r] == 0 and inteiraY[r] >= 10):
                indY[:] = zeroToCrom(indY, cromossomos)
                inteiraY[r] = 10

            if (sinalY[r] == 1 and inteiraY[r] >= 10):
                indY[:] = oneToCrom(indY, cromossomos)
                inteiraY[r] = 10
            pop[r, :] = indX[:]
            pop2[r, :] = indY[:]

        for j in range(pop_size):
            indFit = Individual(realX[j], realY[j])
            fit[j] = indFit.fitnessCalc()
            fitSum = fit[j] + fitSum  # calculando a soma de todos os fits

        # essa linha ja calcula a probabilidade de todos, sem precisar fazer um for por exemplo
        probInd = (1/fitSum)*fit
        newPop_size = 0
        while(newPop_size<pop_size):
            # a roleta em si, n entendi direito mas funciona
            for i in range(pop_size):
                if (i == 0):
                    probtotal[i] = probInd[i]
                else:
                    probtotal[i] = probInd[i]+probtotal[i-1]
    
            jequiti = random.uniform(0, 1)
            p = 0
            while (jequiti > probtotal[p]):
                p = p+1
    
            pai = p
    
            cassino = random.uniform(0, 1)
            p = 0
            while (cassino > probtotal[p]):
                p = p+1
    
            mae = i
    
            while (mae == pai):
                cassino = random.uniform(0, 1)
                p = 0
                while (cassino > probtotal[i]):
                    p = p+1
                mae = p
                
            # -----------------------------------------------------------------    
            # cruza os cria agr
                
            if (pC > random.uniform(0, 1)):
                c = round(1+(cromossomos-2)*random.uniform(0, 1))
                c2 = round(1+(cromossomos-2)*random.uniform(0, 1))
                if (c2 == c):
                    while (c2 == c):
                        c2 = round(1+(cromossomos-2)*random.uniform(0, 1))
                if (c > c2):
                    auxc = 0
                    auxc = c
                    c = c2
                    c2 = auxc
                gene11x = pop[pai][0:c]
                gene12x = pop[pai][c:c2]
                gene13x = pop[pai][c2:cromossomos]
                gene21x = pop[mae][0:c]
                gene22x = pop[mae][c:c2]
                gene23x = pop[mae][c2:cromossomos]
                filhox = numpy.concatenate((gene11x, gene22x, gene13x), axis=None)
                filhax = numpy.concatenate((gene21x, gene12x, gene23x), axis=None)
    
                gene11y = pop2[pai][0:c]
                gene12y = pop2[pai][c:c2]
                gene13y = pop2[pai][c2:cromossomos]
                gene21y = pop2[mae][0:c]
                gene22y = pop2[mae][c:c2]
                gene23y = pop2[mae][c2:cromossomos]
                filhoy = numpy.concatenate((gene11y, gene22y, gene13y), axis=None)
                filhay = numpy.concatenate((gene21y, gene12y, gene23y), axis=None)
                
                
                
                newGenX[newIndX, :] = filhox
                newIndX = newIndX+1
                newGenX[newIndX, :] = filhax
                newIndX = newIndX+1
    
                newGenY[newIndY, :] = filhoy
                newIndY = newIndY+1
                newGenY[newIndY, :] = filhay
                newIndY = newIndY+1
                newPop_size+= 2
                # muta os monstros
                if (pM > random.uniform(0, 1)):
                    m = round(1+(cromossomos-2)*random.uniform(0, 1))
                    if (newGenX[newIndX-2][m] == 0):
                        newGenX[newIndX-2][m] == 1
                    else:
                        newGenX[newIndX-2][m] == 0
                    if (newGenX[newIndX-1][m] == 0):
                        newGenX[newIndX-1][m] == 1
                    else:
                        newGenX[newIndX-1][m] == 0

                    if (newGenY[newIndY-2][m] == 0):
                        newGenY[newIndY-2][m] == 1
                    else:
                        newGenY[newIndY-2][m] == 0
                    if (newGenY[newIndY-1][m] == 0):
                        newGenY[newIndY-1][m] == 1
                    else:
                        newGenY[newIndY-1][m] == 0
                
                
            else:
                auxX = numpy.zeros(cromossomos)
                auxY = numpy.zeros(cromossomos)
                
                auxX2 = numpy.zeros(cromossomos)
                auxY2 = numpy.zeros(cromossomos)
                
                auxX = pop[pai, :]
                auxY = pop2[pai, :]
                
                auxX2 = pop[mae, :]
                auxY2 = pop2[mae, :]
                
                newGenX[newIndX, :] = auxX
                newIndX = newIndX+1
                newGenX[newIndX, :] = auxX2
                newIndX = newIndX+1
    
                newGenY[newIndY, :] = auxY
                newIndY = newIndY+1
                newGenY[newIndY, :] = auxY2
                newIndY = newIndY+1
                newPop_size+= 2
                
            # muta os monstros
        
        #print(newGenX)

        for r in range(newIndX):
            indX[:] = newGenX[r, :]
            indY[:] = newGenY[r, :]

            aux = [int(r) for r in indX]
            aux2 = [int(r) for r in indY]

            sinalX[r] = indX[0]
            sinalY[r] = indY[0]

            inteiraX[r] = convert(aux[1:5])
            inteiraX[r] = binaryTodecimal(inteiraX[r])

            inteiraY[r] = convert(aux2[1:5])
            inteiraY[r] = binaryTodecimal(inteiraY[r])
            
        for r in range(newIndX):
            indX[:] = newGenX[r, :]
            indY[:] = newGenY[r, :]

            if (sinalX[r] == 0 and inteiraX[r] >= 10):
                indX[:] = zeroToCrom(indX, cromossomos)
                inteiraX[r] = 10

            if (sinalX[r] == 1 and inteiraX[r] >= 10):
                indX[:] = oneToCrom(indX, cromossomos)
                inteiraX[r] = 10

            if (sinalY[r] == 0 and inteiraY[r] >= 10):
                indY[:] = zeroToCrom(indY, cromossomos)
                inteiraY[r] = 10

            if (sinalY[r] == 1 and inteiraY[r] >= 10):
                indY[:] = oneToCrom(indY, cromossomos)
                inteiraY[r] = 10
                
            newGenX[r, :] = indX[:]
            newGenY[r, :] = indY[:]
            
            
            
        
            
    chad = 0
    bFit= fit[0]
    
    for p in range(pop_size):
        if (bFit < (fit[p])):
            bFit = fit[p]
            chad = p
    
    bestIndX = numpy.zeros(cromossomos)
    bestIndX = pop[chad, :]
    
    bestIndY = numpy.zeros(cromossomos)
    bestIndY = pop2[chad, :]            
    
    #newPopX[contGen] = bestIndX[:]
    #newPopY[contGen] = bestIndY[:]
    
    newGenX[pop_size-1] = bestIndX[:]
    newGenY[pop_size-1] = bestIndY[:]
        
    elemX = realX[chad]
    elemY = realY[chad]

    pop = newGenX
    pop2 = newGenY
    contGen = contGen+1
    

    
    print("best X = ", elemX)
    print("--------")
    print("best Y = ", elemY)
    print("--------")

    print("best Fit = ", bFit)
    



