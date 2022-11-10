# Codificação : Binaria
# Metodo de seleção: Roleta
# Metodo de cruzamento : dois pontos aleatorios
# Metodo de mutação : binaria
# Elitismo : 1 individuo por geração

import numpy
import random


cromossomos = 30
cc = 0.90
cm = 0.05
numeroger = 30
tamanhopop = 100
ind = numpy.zeros(cromossomos)
ind2 = numpy.zeros(cromossomos)
individuos = numpy.zeros(tamanhopop)
individuos2 = numpy.zeros(tamanhopop)
fit = numpy.zeros(tamanhopop)
novageracao = numpy.zeros((tamanhopop, cromossomos))
novageracao2 = numpy.zeros((tamanhopop, cromossomos))
contadorger = 0
contadorger2 = 0


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


while (contadorger <= numeroger):
    novosindividuos = 0
    while (novosindividuos < (tamanhopop-1)):
        for i in range(tamanhopop):
            ind[:] = pop[i, :]
            conv = 0
            for j in range(cromossomos):
                conv = conv+ind[j]*(2**(cromossomos-(j+1)))
            individuos[i] = (512/(2**cromossomos-1))*conv

while (contadorger2 <= numeroger):
    novosindividuos2 = 0
    while (novosindividuos2 < (tamanhopop-1)):
        for i in range(tamanhopop):
            ind2[:] = pop2[i, :]
            conv = 0
            for j in range(cromossomos):
                conv = conv+ind[j]*(2**(cromossomos-(j+1)))
            individuos2[i] = (512/(2**cromossomos-1))*conv

totalfit = 0
for i in range(tamanhopop):
    fit[i] = -((individuos[i])**2+(individuos2[i])**2) + 4
    totalfit = fit[i]+totalfit

probind = numpy.zeros(tamanhopop)
probtotal = numpy.zeros(tamanhopop)
probind = (1/totalfit)*fit

for i in range(tamanhopop):
    if (i == 0):
        probtotal[i] = probind[i]
    else:
        probtotal[i] = probind[i]+probtotal[i-1]

roleta1 = random.uniform(0, 1)
i = 0
while (roleta1 > probtotal[i]):
    i = i+1

pai = i

roleta2 = random.uniform(0, 1)
i = 0
while (roleta2 > probtotal[i]):
    i = i+1

mae = i

while (mae == pai):
    roleta2 = random.uniform(0, 2)
    i = 0
    while (roleta2 > probtotal[i]):
        i = i+1
    mae = i

if (cc > random.uniform(0, 1)):
    c = round(1+(cromossomos-2)*random.uniform(0, 1))
    genex11 = pop[pai][0:c]
    genex12 = pop[pai][c:cromossomos]
    genex21 = pop[mae][0:c]
    genex22 = pop[mae][c:cromossomos]
    filhox1 = numpy.concatenate((genex11, genex22), axis=None)
    filhox2 = numpy.concatenate((genex21, genex12), axis=None)

    geney11 = pop2[pai][0:c]
    geney12 = pop2[pai][c:cromossomos]
    geney21 = pop2[mae][0:c]
    geney22 = pop2[mae][c:cromossomos]
    filhoy1 = numpy.concatenate((geney11, geney22), axis=None)
    filhoy2 = numpy.concatenate((geney21, geney12), axis=None)

    novageracao[novosindividuos, :] = filhox1
    novosindividuos = novosindividuos+1
    novageracao[novosindividuos, :] = filhox2
    novosindividuos = novosindividuos+1

    novageracao2[novosindividuos2, :] = filhoy1
    novosindividuos2 = novosindividuos2+1
    novageracao2[novosindividuos2, :] = filhoy1
    novosindividuos2 = novosindividuos2+1


if (cm > random.uniform(0, 1)):
    d = round(1+(cromossomos-2)*random.uniform(0, 1))
    if (novageracao[novosindividuos-2][d] == 0):
        novageracao[novosindividuos-2][d] = 1
    else:
        novageracao[novosindividuos-2][d] = 0
    if (novageracao2[novosindividuos2-2][d] == 0):
        novageracao2[novosindividuos2-2][d] = 1
    else:
        novageracao2[novosindividuos2-2][d] = 0
    if (novageracao[novosindividuos-1][d] == 0):
        novageracao[novosindividuos-1][d] = 1
    else:
        novageracao[novosindividuos-1][d] = 0
    if (novageracao2[novosindividuos2-1][d] == 0):
        novageracao2[novosindividuos2-1][d] = 1
    else:
        novageracao2[novosindividuos2-1][d] = 0

indice = fit.argmax()
elem = individuos[indice]
contadorger = contadorger+1
contadorger2 = contadorger2+1
print(elem)
