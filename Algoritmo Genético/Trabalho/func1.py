# Desenvolver uma solução de Otimização Combinatória
# com abordagem de um Algoritmo Genético
# Codificação: Binária      Seleção: Roleta
# Cruzamento: Dois Pontos   Mutação: Binária
# Elitismo: 1 indivíduo por Geração

# Função de Otimização: 𝑍 = −(𝑥² + y²) +4
# Restrições:    x ∈ [-10, 10] && y ∈ [-10, 10]

import random as rd
import numpy as np
import matplotlib as plt
# import fixedPoint as fp

xRange = [-10, 10]
yRange = [-10, 10]
pC = 0.75
pM = 0.025

sizeSignal = 1
sizeInt = 4
sizeFlt = 25

sizePop = 100

numGenerations = 100
generation = 0


class individual:
    def __init__(initX, initY):
        self.x = initX
        self.y = initY

    def fitnessCalc(self):
        Z = -(self.x**2 + self.y**2) + 4
        return Z


class individualX:
    popSignalX = np.zeros((sizePop, sizeSignal))
    for i in range(sizePop):
        for j in range(sizeSignal):
            a = rd.uniform(0, 1)
            if (a >= 0.5):
                popSignalX[i][j] = 1
            else:
                popSignalX[i][j] = 0

    popIntX = np.zeros((sizePop, sizeInt))
    for i in range(sizePop):
        for j in range(sizeInt):
            a = rd.uniform(0, 1)
            if (a >= 0.5):
                popIntX[i][j] = 1
            else:
                popIntX[i][j] = 0

    popFltX = np.zeros((sizePop, sizeFlt))
    for i in range(sizePop):
        for j in range(sizeFlt):
            a = rd.uniform(0, 1)
            if (a >= 0.5):
                popFltX[i][j] = 1
            else:
                popFltX[i][j] = 0


class individualY:
    popSignalY = np.zeros((sizePop, sizeSignal))
    for i in range(sizePop):
        for j in range(sizeSignal):
            a = rd.uniform(0, 1)
            if (a >= 0.5):
                popSignalY[i][j] = 1
            else:
                popSignalY[i][j] = 0

    popIntY = np.zeros((sizePop, sizeInt))
    for i in range(sizePop):
        for j in range(sizeInt):
            a = rd.uniform(0, 1)
            if (a >= 0.5):
                popIntY[i][j] = 1
            else:
                popIntY[i][j] = 0

    popFltY = np.zeros((sizePop, sizeFlt))
    for i in range(sizePop):
        for j in range(sizeFlt):
            a = rd.uniform(0, 1)
            if (a >= 0.5):
                popFltY[i][j] = 1
            else:
                popFltY[i][j] = 0

        # new individual.__init__(x, y)

        # # for j in range(xRange):
        # #     a = random.uniform(0, 1):
        # #     if (a >= 0.5):
        # #         p[i][j] = 1
        # #     # else:
        # #     #     p[i][j] = 0

# newGeneration = np.zeros((sizePop, sizeC))
# ind = np.zeros(sizeC)

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


# while (generation <= numGenerations):
#     novosindividuos = 0
#     while (novosindividuos < (sizePop-1)):
#         for i in range(sizePop):
#             for j in range(sizeC):

#                 #  ind[:] = pop[i,: j]
