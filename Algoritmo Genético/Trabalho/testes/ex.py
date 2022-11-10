import time
import re
import random
import numpy as np
import math
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys


num_individuos = 10
populacao = []
populacao_filhos = []
geracao = 1
maior_nota = 0


def converte_b_2_d(n):  # Converte binario para decimal
    decimal = 0
    n = str(n)
    n = n[::-1]
    tam = len(n)
    for i in range(tam):
        if n[i] == "1":
            decimal = decimal + 2**i
    return decimal


def funcao_ativacao(x, y):  # formula dada no problema
    return abs(x*math.sin(y*math.pi/4) + y*math.sin(x*math.pi/4))


def gera_pop():  # Gera inha população inicial de individuos
    global num_individuos, populacao
    for i in range(0, num_individuos):
        individuo = ''
        for j in range(0, 20):
            # gera numeros aleatorios dando 50% de ser 0 e 50% de ser 1
            a = random.randint(0, 10)
            if a >= 5:
                individuo += '1'
            else:
                individuo += '0'
        # adiciona a string a população
        populacao.append(individuo)


# Usa a formula dos slides para converter os intervalos
def converter_intervalo(numero):
    '''forma da equaçao
    real = inf + (sup - inf)/(2^k-1)*r
    equaçao simplificada
    '''
    return 0.019550342*numero


def gera_pop_filhos(i):
    global populacao, populacao_filhos, geracao, maior_nota, nota_max
    nota = []
    melhor_individuo = ''
    melhor_individuo_nota = ''

    # Calculando fitness

    # Separando x e y de cada individuo
    populacao_dec_x = []
    populacao_dec_y = []

    for i in range(0, num_individuos):
        aux_x = ''
        aux_y = ''
        for j in range(0, 10):
            aux_x += populacao[i][j]
            aux_y += populacao[i][j+10]

        populacao_dec_x.append(aux_x)
        populacao_dec_y.append(aux_y)
    # Passando cada individuo pela função de avaliação
    for i in range(0, num_individuos):

        populacao_dec_x[i] = converte_b_2_d(populacao_dec_x[i])
        populacao_dec_y[i] = converte_b_2_d(populacao_dec_y[i])
        populacao_dec_x[i] = converter_intervalo(populacao_dec_x[i])
        populacao_dec_y[i] = converter_intervalo(populacao_dec_y[i])
        # armazena a nota de cada individuo
        nota.append(funcao_ativacao(populacao_dec_x[i], populacao_dec_y[i]))

    # Montando roleta

    soma = sum(nota)
    # cria uma matriz de char com cada "slot" tendo 10 espaçoes
    tabela_cruzamento = np.chararray(
        (math.ceil(num_individuos/2), 2), itemsize=20, unicode=False)

    for i in range(0, math.ceil(num_individuos/2)):
        for j in range(0, 2):
            # girando a roleta
            s = random.randint(1, math.floor(soma)-1)
            ind = 0
            aux = nota[ind]
            while (aux < s):
                ind += 1
                aux += nota[ind]
            # selecionei o individuo e tou colocando ele na tabela pra cruzar dps
            tabela_cruzamento[i][j] = populacao[ind]
    # como a função da numpy salva como bytes tem que decodificar de volta pra string
    tabela_cruzamento = tabela_cruzamento.decode('utf-8')

    # Crusar os individuos

    for i in range(0, math.ceil(num_individuos/2)):
        aux_1 = ''
        aux_2 = ''
        aux_3 = ''
        aux_4 = ''
        # sorteio de onde será o corte
        s = random.randint(1, 19)

        for j in range(0, s):
            aux_1 += tabela_cruzamento[i][0][j]  # ind1 parte1
            aux_2 += tabela_cruzamento[i][1][j]  # ind2 parte1
        for j in range(s, 20):
            aux_3 += tabela_cruzamento[i][0][j]  # ind1 parte2
            aux_4 += tabela_cruzamento[i][1][j]  # ind2 parte2

        populacao_filhos.append(aux_1+aux_4)
        populacao_filhos.append(aux_2+aux_3)

    # Aplicar mutaçao

    for i in range(0, num_individuos):
        # para cada individuo sorteia um numero se ele for menor que 5 ocorrerá mutação
        s = random.randint(1, 100)
        if s < 5:
            # sorteio aleatorio do indice que será mutado
            indice = random.randint(0, 19)
            if indice == 0:
                a = str(populacao_filhos[i][1:])

                if populacao_filhos[i][indice] == '0':

                    populacao_filhos[i] = "1"+a
                else:

                    populacao_filhos[i] = "0"+a

            if indice == 1:

                a = str(populacao_filhos[i][2:])
                b = str(populacao_filhos[i][0])

                if populacao_filhos[i][indice] == '0':

                    populacao_filhos[i] = b+"1"+a

                else:

                    populacao_filhos[i] = b+"0"+a
            else:
                if populacao_filhos[i][indice] == '0':

                    a = str(populacao_filhos[i][0:indice-1])
                    b = str((populacao_filhos[i][indice:]))
                    populacao_filhos[i] = a + "1"+b

                if populacao_filhos[i][indice] == '1':

                    a = str(populacao_filhos[i][0:indice-1])
                    b = str((populacao_filhos[i][indice:]))
                    populacao_filhos[i] = a + "0" + b
        else:
            continue

    # Configuraçoes basicas para exibir no grafico
    # pego a maior nota da geração
    fit = sorted(nota)
    maior_nota = fit[num_individuos-1]

    # acha quem é o melhor individuo e qual sua nota e coloca em variaveis golbais e printa no terminal
    for i in range(0, num_individuos):
        if nota[i] == maior_nota:
            x = converte_b_2_d(populacao[i][0:10])

            y = converte_b_2_d(populacao[i][10:])

            x = converter_intervalo(x)

            y = converter_intervalo(y)
            melhor_individuo = str(populacao[i])
            melhor_individuo_nota = str(funcao_ativacao(x, y))
            print('GERAÇÃO: ', geracao)
            print("\nMelhor individuo: ",
                  populacao[i], "\nCom Fitness: ", funcao_ativacao(x, y), "\n")

    # zero minha propulação para a prox iteração
    populacao = []

    # adiciono a populaçao de filhos gerada a população atual
    for i in range(0, num_individuos):
        populacao.append(populacao_filhos[i])

    # zero a população de filhos pois todos estao na população atual
    populacao_filhos = []

    # gerando os pontos para plotagem 3D da função dada na questão
    X = np.outer(np.linspace(0, 20, 100), np.ones(100))
    Y = X.copy().T  # transpose
    Z = np.absolute(X*np.sin(Y*np.pi/4) + Y*np.sin(X*np.pi/4))
    # configurando os graficos
    ax = plt.axes(projection='3d')
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
    ax.scatter(populacao_dec_x, populacao_dec_y, nota, color='black')
    ax.set_title('GERAÇÃO: ' + str(geracao)+"\nMelhor individuo: " +
                 str(melhor_individuo)+"\nCom Fitness: "+str(melhor_individuo_nota)+"\n")

    # USADO PARA LIMITAR QUANTAS GERAÇÕES PODEM EXISTIR POR TESTE COM 100 INDIVIDUOS ELES   CONVERGEM
    # PARA O MAXIMO ENTRE 20 E 30 GERAÇÕES COM 10 INDIVIDUOS CONVERGEM PARA UM MAXIMO ENTRE 5 E 15 GERAÇÕES
    # POREM PARA MELHOR VISUALIZAÇÃO COLQUEI O PADRAO "INFINITO" OU ATÉ SER PARADO CASO QUEIRA LIMITAR UM
    # NUMERO MAXIMO DE GERAÇOES DESCOMENTE O CODIGO ABAIXO E TROQUE O VALOR 10 PELO DESEJADO
    # if geracao > 10:
    #    sys.exit()
    geracao += 1


def gera_grafico():
    gera_pop()
    # gera um objeto para a plotagem dos graficos
    fig = plt.figure()
    # faz com que os graficos atualizem na mesma tela com um delay de 3000ms ou 3s
    ani = animation.FuncAnimation(fig, gera_pop_filhos, interval=3000)
    # "imprime" os graficos
    plt.show(ani)


gera_grafico()
