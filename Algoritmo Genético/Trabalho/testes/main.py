import numpy
import random
from Individual import Individual


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


def zeroToCrom(list):
    for i in range(cromossomos):
        if (i == 1 or i == 3):
            list[i] = 1
        else:
            list[i] = 0
    return list


def oneToCrom(list):
    for i in range(cromossomos):
        if (i == 0 or i == 1 or i == 3):
            list[i] = 1
        else:
            list[i] = 0
    return list


cromossomos = 30
pC = 0.90
pM = 0.05
gen = 10
pop_size = 10
contadorger = 0
contadorger2 = 0
fitsum = 0


# nomenclaturas: sem numero é X, com 2 é Y
# ind: individuo passageiro
# sinal: sinal do numero
# inteira: parte inteira do numero
# decimal: parte decimal do numero
# real: numero em si
# fit: fit do numero na função
# novageração: aux para geração

indX = numpy.zeros(cromossomos)
indY = numpy.zeros(cromossomos)

indB = numpy.zeros(cromossomos)
indB2 = numpy.zeros(cromossomos)

sinalX = numpy.zeros(pop_size)
sinalY = numpy.zeros(pop_size)

inteiraX = numpy.zeros(pop_size)
inteiraY = numpy.zeros(pop_size)

realX = numpy.zeros(pop_size)
realY = numpy.zeros(pop_size)

decimalX = numpy.zeros(pop_size)
decimalY = numpy.zeros(pop_size)

fit = numpy.zeros(pop_size)

novageracao = numpy.zeros((pop_size, cromossomos))
novageracao2 = numpy.zeros((pop_size, cromossomos))


# def getFitSum():
#     fitsum = sum([indFit.getFitness() for ind in self.population])
#     return self.fitsum


pop = numpy.zeros((pop_size, cromossomos))
for i in range(pop_size):
    for j in range(cromossomos):
        a = random.uniform(0, 1)
        if (a >= 0.5):
            pop[i][j] = 1
        else:
            pop[i][j] = 0

pop2 = numpy.zeros((pop_size, cromossomos))
for h in range(pop_size):
    for t in range(cromossomos):
        a = random.uniform(0, 1)
        if (a >= 0.5):
            pop2[h][t] = 1
        else:
            pop2[h][t] = 0

newPop = numpy.zeros((pop_size, cromossomos))
newPop2 = numpy.zeros((pop_size, cromossomos))

# while(contadorger<=numeroger):
novosindividuos = 0
novosindividuos2 = 0
# while(novosindividuos<(pop_size-1)):


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

    # if (sinal[r] == 0 and inteira[r] >= 10):
    #     ind[r] = zeroToCrom(ind[r])
    #     inteira[r] = 10

    # if (sinal[r] == 1 and inteira[r] >= 10):
    #     ind[r] = oneToCrom(ind[r])
    #     inteira[r] = 10

    # if (sinal2[r] == 0 and inteiraY[r] >= 10):
    #     ind2[r] = zeroToCrom(ind2[r])
    #     inteiraY[r] = 10

    # if (sinal2[r] == 1 and inteiraY[r] >= 10):
    #     ind2[r] = oneToCrom(ind2[r])
    #     inteiraY[r] = 10

for r in range(pop_size):
    indX[:] = pop[r, :]
    indY[:] = pop2[r, :]

    if (sinalX[r] == 0 and inteiraX[r] >= 10):
        indX[:] = zeroToCrom(indX)
        inteiraX[r] = 10

    if (sinalX[r] == 1 and inteiraX[r] >= 10):
        indX[:] = oneToCrom(indX)
        inteiraX[r] = 10

    if (sinalY[r] == 0 and inteiraY[r] >= 10):
        indY[:] = zeroToCrom(indY)
        inteiraY[r] = 10

    if (sinalY[r] == 1 and inteiraY[r] >= 10):
        indY[:] = oneToCrom(indY)
        inteiraY[r] = 10
    pop[r, :] = indX[:]
    pop2[r, :] = indY[:]


for j in range(pop_size):
    indFit = Individual(realX[j], realY[j])
# print(indFit.fitnessCalc())

    fit[j] = indFit.fitnessCalc()

print(fit)
