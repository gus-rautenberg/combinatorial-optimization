import random
import numpy


def binaryTodecimal(n):  # função de converção binaria para decimal
    decimal = 0
    power = 1
    while n > 0:
        rem = n % 10
        n = n//10
        decimal += rem*power
        power = power*2
    return decimal


def convert(list):  # função de converter uma lista de um tipo, para uma lista de inteiro
    res = int("".join(map(str, list)))
    return res


def numConcat(num1, num2):  # função para concatenar listas
    digits = len(str(num2))
    num1 = num1 * (10**digits)
    num1 += num2
    return num1


def zeroToCrom(list, num1):
    for i in range(num1):
        if (i == 1 or i == 3):
            list[i] = 1
        else:
            list[i] = 0
    return list


def initInd(list, num1):
    for j in range(num1):
        a = random.uniform(0, 1)
        if (a >= 0.5):
            list[j] = 1
        else:
            list[j] = 0
    return list


def arredondar(list, num1):
    aux = initInd(list, num1)
    return aux


def oneToCrom(list, num1):
    for i in range(num1):
        if (i == 0 or i == 1 or i == 3):
            list[i] = 1
        else:
            list[i] = 0
    return list


def initPop(list, num1, num2):
    for i in range(num1):
        for j in range(num2):
            a = random.uniform(0, 1)
            if (a >= 0.5):
                list[i][j] = 1
            else:
                list[i][j] = 0
    return list


def binToDec(pop_size, cromossomos, pop, pop2, bestRealX, bestRealY, indX, indY, sinalX, sinalY, realX, realY, g3x):
    for i in range(pop_size):
        indX[:] = pop[i, :]
        indY[:] = pop2[i, :]
        auxConv = 0
        auxConv2 = 0
        sinalX[i] = indX[0]
        sinalY[i] = indY[0]

        for j in range(cromossomos):
            auxConv = auxConv+indX[j]*(2**(cromossomos-(j+1)))
            auxConv2 = auxConv2+indY[j]*(2**(cromossomos-(j+1)))

            realX[i] = (10/(2**cromossomos-1))*auxConv
            realY[i] = (10/(2**cromossomos-1))*auxConv2

            if (sinalX[i] == 1):
                realX[i] = realX[i]*-1
            if (sinalY[i] == 1):
                realY[i] = realY[i]*-1
            if (g3x > 0):
                realX[pop_size-1] = bestRealX
                realY[pop_size-1] = bestRealY
