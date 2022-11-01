import numpy
import random


class individual:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def fitnessnessCalc(self):
        Z = -(self.x**2 + self.y**2) + 4
        return Z


class algorithm:
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

    cromossomos = 30
    cc = 0.90
    cm = 0.05
    numeroger = 10
    tamanhopop = 10
    contadorger = 0
    contadorger2 = 0

    # nomenclaturas: sem numero é X, com 2 é Y
    # ind: individuo passageiro
    # sinal: sinal do numero
    # inteira: parte inteira do numero
    # decimal: parte decimal do numero
    # real: numero em si
    # fit: fit do numero na função
    # novageração: aux para geração

    ind = numpy.zeros(cromossomos)
    ind2 = numpy.zeros(cromossomos)
    sinalX = numpy.zeros(tamanhopop)
    sinalY = numpy.zeros(tamanhopop)

    inteiraX = numpy.zeros(tamanhopop)
    inteiraY = numpy.zeros(tamanhopop)

    realX = numpy.zeros(tamanhopop)
    realY = numpy.zeros(tamanhopop)

    decimalX = numpy.zeros(tamanhopop)
    decimalY = numpy.zeros(tamanhopop)

    fitness = numpy.zeros(tamanhopop)

    novageracao = numpy.zeros((tamanhopop, cromossomos))
    novageracao2 = numpy.zeros((tamanhopop, cromossomos))

    pop = numpy.zeros((tamanhopop, cromossomos))
    for i in range(tamanhopop):
        for j in range(cromossomos):
            a = random.uniform(0, 1)
            if (a >= 0.5):
                pop[i][j] = 1
            else:
                pop[i][j] = 0

    pop2 = numpy.zeros((tamanhopop, cromossomos))
    for h in range(tamanhopop):
        for t in range(cromossomos):
            a = random.uniform(0, 1)
            if (a >= 0.5):
                pop2[h][t] = 1
            else:
                pop2[h][t] = 0

    # while(contadorger<=numeroger):
    novosindividuos = 0
    novosindividuos2 = 0
    # while(novosindividuos<(tamanhopop-1)):
    for i in range(tamanhopop):
        ind[:] = pop[i, :]
        ind2[:] = pop2[i, :]
        aux = [int(i) for i in ind]
        aux2 = [int(i) for i in ind2]

        sinalX[i] = ind[0]
        sinalY[i] = ind2[0]

        inteiraX[i] = convert(aux[1:5])
        inteiraX[i] = binaryTodecimal(inteiraX[i])

        inteiraY[i] = convert(aux2[1:5])
        inteiraY[i] = binaryTodecimal(inteiraY[i])

        decimalX[i] = convert(aux[6:30])
        decimalX[i] = binaryTodecimal(decimalX[i])

        decimalY[i] = convert(aux2[6:30])
        decimalY[i] = binaryTodecimal(decimalY[i])
        intinteira = [int(i) for i in inteiraX]
        intdecimal = [int(i) for i in decimalX]
        intinteiraY = [int(i) for i in inteiraY]
        intdecimalY = [int(i) for i in decimalY]

    for r in range(tamanhopop):
        digits = 0
        base = 10
        # print(intinteira[r])
        # print(intdecimal[r])
        realX[r] = numConcat(intinteira[r], intdecimal[r])
        # print(XrealX[r])
        # intrealX=[int(r) for r in real]
        if (intinteira[r] < 10 and intinteira[r] > 0):
            # print(realX[r])
            digits = len(str(realX[r]))
            realX = realX[r]/(base**(digits-3))
            # print("-----------------------------=")
            # print(realX[r])
        if (intinteira[r] >= 10):
            digits = len(str(realX[r]))
            realX[r] = realX[r]/(base**(digits-4))
        if (intinteira[r] == 0):
            digits = len(str(realX[r]))
            realX[r] = realX[r]/(base**(digits-2))

        digits2 = 0
        base2 = 10
        realY[r] = numConcat(intinteiraY[r], intdecimalY[r])
        if (intinteiraY[r] >= 10):
            digits2 = len(str(realY[r]))
            realY[r] = realY[r]/(base2**(digits2-4))
        if (intinteiraY[r] == 0):
            digits2 = len(str(realY[r]))
            realY[r] = realY[r]/(base2**(digits2-2))
        if (intinteiraY[r] < 10 or intinteiraY[r] > 0):
            digits2 = len(str(realY[r]))
            realY[r] = realY[r]/(base2**(digits2-3))
        if (sinalX[r] == 1):
            realX[r] = realX[r]*-1
        if (sinalY[r] == 1):
            realY[r] = realY[r]*-1

    for j in range(tamanhopop):
        indFit = individual(realX[j], realY[j])
    # print(indfitness.fitnessnessCalc())
    fitness[j] = indFit.fitnessCalc()

    print(fitness)
