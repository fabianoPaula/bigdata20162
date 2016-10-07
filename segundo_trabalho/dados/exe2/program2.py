#!/usr/bin/env python2.7
# -*- coding: utf-8 -*

from scipy.stats import chi2_contingency as chi2
import csv
import matplotlib.pyplot as plt

X = []
Y = []


def calc(file):
    count_yes = 0
    count_no = 0
    csvfile = open(file, 'rb') 
    spamreader = csv.reader(csvfile, delimiter=';')
    next(spamreader,None) # Pula a primeira linha
    for row in spamreader:
	if( row[1] == 'yes' ):
	    count_yes += 1
	elif(row[1] == 'no'):
	    count_no += 1
	else:
	    print("Vazio!")
    return(count_yes,count_no)


A_yes,A_no = calc("amostra_A_click.csv")
B_yes,B_no = calc("amostra_B_click.csv")



print A_yes,A_no 
print B_yes,B_no

M = [[A_yes,A_no],[B_yes,B_no]]

est, p_value, dof, exp = chi2(M)
print("Grau de confiança é 97%. Precisamos de p-value > 0.03 para não rejeitar H0 ")
print("Estátisitica de teste: %f;\np-valor: %f;\n Graus de liberdade: %d" % (est,p_value,dof))
print("Esperado: ")
print(exp[0,0],exp[0,1])
print(exp[1,0],exp[1,1])

