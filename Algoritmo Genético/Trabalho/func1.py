# Desenvolver uma solução de Otimização Combinatória
# com abordagem de um Algoritmo Genético
# Codificação: Binária      Seleção: Roleta
# Cruzamento: Dois Pontos   Mutação: Binária
# Elitismo: 1 indivíduo por Geração

# Função de Otimização: 𝑍 = −(𝑥² + y²) +4
# Restrições:    x ∈ [-10, 10] && y ∈ [-10, 10]

import random
import numpy as np
import matplotlib as plt
import fixedPoint as fp

xRange = [-10, 10]
yRange = [-10, 10]
pC = 0.75
pM = 0.025


sizeInt = 4

sizePop = 100

numGenerations = 100
generation = 0


class individual:
    def __init__(self initX, initY):
        self.x = initX
        self.y = initY

    def fitnessCalc(self):
        Z = -(self.x**2 + self.y**2) + 4
        return Z


pop = np.zeros((sizePop, xRange))
for i in range(sizePop):
    x = random.randrange(-10, 10)
    y = random.randrange(-10, 10)

    new individual.__init__(x, y)

    # for j in range(xRange):
    #     a = random.uniform(0, 1):
    #     if (a >= 0.5):
    #         p[i][j] = 1
    #     # else:
    #     #     p[i][j] = 0

newGeneration = np.zeros((sizePop, sizeC))
ind = np.zeros(sizeC)

# Função binToDec


def binToDec(bin):

    bin1 = bin
    decimal = 0
    i = 0
    n = 0
    while (bin != 0):
        dec = bin % 10
        decimal = decimal + dec * pow(2, i)
        bin = bin//10
        i += 1
    return decimal


while (generation <= numGenerations):
    novosindividuos = 0
    while (novosindividuos < (sizePop-1)):
        for i in range(sizePop):
            for j in range(sizeC):

                #  ind[:] = pop[i,:]
