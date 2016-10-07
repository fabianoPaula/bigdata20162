#!/usr/bin/env python2.7
# -*- coding: utf-8 -*

#import numpy as np
from numpy import sqrt
import csv
import matplotlib.pyplot as plt

soma_total = 0.0
tamanho_populacao = 0

# Para calcular a média da população
with open('populacao_tempo.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='\n')
    next(spamreader,None)
    for row in spamreader:
        soma_total += float(row[1])
        tamanho_populacao += 1

print("Tamanho da População: %d" % (tamanho_populacao))

media_populacao = soma_total/tamanho_populacao

soma_total = 0.0

# Para calcular a variância e o desvio padrão
with open('populacao_tempo.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='\n')
    next(spamreader,None)
    for row in spamreader:
        soma_total += (media_populacao - float(row[1]))**2

variancia = soma_total/(tamanho_populacao - 1)
desvio_padrao = sqrt(variancia)

print("Média da População: %f" % (media_populacao))
print("Variância da População: %f" % (variancia))
print("Desvio Padrão da População: %f\n" % (desvio_padrao))
print("Ganho na média: R$ %.2f\n " % (media_populacao*0.05))

print("----------------------------------------------------------\n")

soma_amostra = 0.0
tamanho_amostra = 0

# Para calcular a variância e o desvio padrão
with open('amostra_tempo.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='\n')
    next(spamreader,None)
    for row in spamreader:
	soma_amostra += float(row[1])
	tamanho_amostra += 1

print("Tamanho da Amostra: %d" % (tamanho_amostra))
media_amostra = soma_amostra/tamanho_amostra

print("Média da Amostra: %f" % (media_amostra))
print("Ganho na média: R$ %.2f" % (media_amostra*0.05))


def avalia_amostra(limite_superior, limite_inferior,media_amostra):
    print("Limite superior de aceitação da média: %f" % (limite_superior))
    print("Limite inferior de aceitação da média: %f\n" % (limite_inferior))

    if ( limite_inferior < media_amostra and limite_superior > media_amostra):
	print("H0: Não rejeitada: Feature indiferente")
    elif(limite_inferior > media_amostra):
	print("H0: Rejeitada: Feature diminuiu a media de tempo do usuario")
    elif( limite_superior < media_amostra):
	print("H0: Não Rejeitada: Feature aumentou o tempo do usuario")
    print("\n----------------------------------------------------------\n\n")



limite_superior = media_populacao + 1.96*desvio_padrao/sqrt(tamanho_populacao)
limite_inferior = media_populacao - 1.96*desvio_padrao/sqrt(tamanho_populacao)

avalia_amostra(limite_superior,limite_inferior,media_amostra)

limite_superior = media_populacao + 1.65*desvio_padrao/sqrt(tamanho_populacao)
limite_inferior = media_populacao - 1.65*desvio_padrao/sqrt(tamanho_populacao)

avalia_amostra(limite_superior,limite_inferior,media_amostra)

limite_superior = media_populacao + 1.52*desvio_padrao/sqrt(tamanho_populacao)
limite_inferior = media_populacao - 1.52*desvio_padrao/sqrt(tamanho_populacao)

avalia_amostra(limite_superior,limite_inferior,media_amostra)
