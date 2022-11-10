import numpy
import random


def binaryTodecimal(n):
    decimal = 0
    power = 1
    while n > 0:
        rem = n % 10
        n = n//10
        decimal += rem*power
        power = power*2
    return decimal


def convert(list):
    res = int("".join(map(str, list)))
    return res


cromossomos = 30
cc = 0.90
cm = 0.05
numeroger = 10
tamanhopop = 10
tamanhopop2 = 10
contadorger = 0
contadorger2 = 0
intrange = 4
j = 0


ind = numpy.zeros(cromossomos)
ind2 = numpy.zeros(cromossomos)
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


pop = numpy.zeros((tamanhopop, cromossomos))
for i in range(tamanhopop):
    for j in range(cromossomos):
        a = random.uniform(0, 1)
        if (a >= 0.5):
            pop[i][j] = 1
        else:
            pop[i][j] = 0

pop2 = numpy.zeros((tamanhopop, cromossomos))
for i in range(tamanhopop):
    for j in range(cromossomos):
        a = random.uniform(0, 1)
        if (a >= 0.5):
            pop2[i][j] = 1
        else:
            pop2[i][j] = 0


# while(contadorger<=numeroger):
        novosindividuos = 0
        novosindividuos2 = 0
    # while(novosindividuos<(tamanhopop-1)):
        for i in range(tamanhopop):
            ind[:] = pop[i, :]
            # ind2[:]=pop2[i,:]
            aux = [int(i) for i in ind]
            # aux2= [int(t) for t in ind2]
            sinal[i] = ind[0]
            # sinal2[i]=ind2[0]
            inteira[i] = convert(aux[1:5])
            inteira[i] = binaryTodecimal(inteira[i])
            # inteira2[i]=convert(aux2[1:5])
            # inteira2[i]=binaryTodecimal(inteira2[i])
            decimal[i] = convert(aux[6:30])
            decimal[i] = binaryTodecimal(decimal[i])
            # decimal2[i]=convert(aux2[6:30])
            # decimal2[i]=binaryTodecimal(decimal2[i])
        for j in range(tamanhopop2):
            ind2[:] = pop2[j, :]
            aux2 = [int(j) for j in ind2]
            sinal2[j] = ind2[0]
            inteira2[j] = convert(aux2[1:5])
            print(inteira2[i])
            inteira2[j] = binaryTodecimal(inteira2[j])
            decimal2[j] = convert(aux2[6:30])
            decimal2[j] = binaryTodecimal(decimal2[j])
