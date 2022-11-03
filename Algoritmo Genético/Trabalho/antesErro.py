import numpy
import random


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
indB = numpy.zeros(cromossomos)
indB2 = numpy.zeros(cromossomos)
sinal = numpy.zeros(tamanhopop)
sinal2 = numpy.zeros(tamanhopop)
inteira = numpy.zeros(tamanhopop)
inteira2 = numpy.zeros(tamanhopop)
real = numpy.zeros(tamanhopop)
real2 = numpy.zeros(tamanhopop)
decimal = numpy.zeros(tamanhopop)
decimal2 = numpy.zeros(tamanhopop)
fit = numpy.zeros(tamanhopop)
novageracao = numpy.zeros((tamanhopop, cromossomos))
novageracao2 = numpy.zeros((tamanhopop, cromossomos))


class individual:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def fitnessCalc(self):
        Z = -(self.x**2 + self.y**2) + 4
        return Z


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

newPop = numpy.zeros((tamanhopop, cromossomos))
newPop2 = numpy.zeros((tamanhopop, cromossomos))

# while(contadorger<=numeroger):
novosindividuos = 0
novosindividuos2 = 0
# while(novosindividuos<(tamanhopop-1)):


for i in range(tamanhopop):
    ind[:] = pop[i, :]
    ind2[:] = pop2[i, :]

    aux = [int(i) for i in ind]
    aux2 = [int(i) for i in ind2]

    sinal[i] = ind[0]
    sinal2[i] = ind2[0]

    inteira[i] = convert(aux[1:5])
    inteira[i] = binaryTodecimal(inteira[i])

    inteira2[i] = convert(aux2[1:5])
    inteira2[i] = binaryTodecimal(inteira2[i])

    decimal[i] = convert(aux[6:30])
    decimal[i] = binaryTodecimal(decimal[i])

    decimal2[i] = convert(aux2[6:30])
    decimal2[i] = binaryTodecimal(decimal2[i])

    intinteira = [int(i) for i in inteira]
    intdecimal = [int(i) for i in decimal]

    intinteira2 = [int(i) for i in inteira2]
    intdecimal2 = [int(i) for i in decimal2]


for r in range(tamanhopop):

    aux = [int(r) for r in ind]
    aux2 = [int(r) for r in ind2]

    digits = 0
    base = 10
    # print(intinteira[r])
    # print(intdecimal[r])
    real[r] = numConcat(intinteira[r], intdecimal[r])
    # print(real[r])
    # intreal=[int(r) for r in real]
    if (intinteira[r] >= 10):
        real[r] = 10

    if (intinteira[r] < 10 and intinteira[r] > 0):
        # print(real[r])
        digits = len(str(real[r]))
        real[r] = real[r]/(base**(digits-3))
        # print("-----------------------------=")
        # print(real[r])

    if (intinteira[r] == 0):
        digits = len(str(real[r]))
        real[r] = real[r]/(base**(digits-2))

    digits2 = 0
    base2 = 10
    real2[r] = numConcat(intinteira2[r], intdecimal2[r])
    if (intinteira2[r] >= 10):
        real2[r] = 10

    if (intinteira2[r] == 0):
        digits2 = len(str(real2[r]))
        real2[r] = real2[r]/(base2**(digits2-2))

    if (intinteira2[r] < 10 and intinteira2[r] > 0):
        digits2 = len(str(real2[r]))
        real2[r] = real2[r]/(base2**(digits2-3))

    if (sinal[r] == 1):
        real[r] = real[r]*-1

    if (sinal2[r] == 1):
        real2[r] = real2[r]*-1

    # if (sinal[r] == 0 and inteira[r] >= 10):
    #     ind[r] = zeroToCrom(ind[r])
    #     inteira[r] = 10

    # if (sinal[r] == 1 and inteira[r] >= 10):
    #     ind[r] = oneToCrom(ind[r])
    #     inteira[r] = 10

    # if (sinal2[r] == 0 and inteira2[r] >= 10):
    #     ind2[r] = zeroToCrom(ind2[r])
    #     inteira2[r] = 10

    # if (sinal2[r] == 1 and inteira2[r] >= 10):
    #     ind2[r] = oneToCrom(ind2[r])
    #     inteira2[r] = 10

for r in range(tamanhopop):
    ind[:] = pop[r, :]
    ind2[:] = pop2[r, :]

    if (sinal[r] == 0 and inteira[r] >= 10):
        ind[:] = zeroToCrom(ind)
        inteira[r] = 10

    if (sinal[r] == 1 and inteira[r] >= 10):
        ind[:] = oneToCrom(ind)
        inteira[r] = 10

    if (sinal2[r] == 0 and inteira2[r] >= 10):
        ind2[:] = zeroToCrom(ind2)
        inteira2[r] = 10

    if (sinal2[r] == 1 and inteira2[r] >= 10):
        ind2[:] = oneToCrom(ind2)
        inteira2[r] = 10
    pop[r, :] = ind[:]
    pop2[r, :] = ind2[:]


for j in range(tamanhopop):
    indFit = individual(real[j], real2[j])
# print(indFit.fitnessCalc())
    fit[j] = indFit.fitnessCalc()

print(fit)
