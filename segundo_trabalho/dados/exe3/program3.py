#!/usr/bin/env python2.7
# -*- coding: utf-8 -*

from scipy.stats import spearmanr as sp
import csv

X = []
Y = []

count = 0
total = 0

# Para calcular a média da população
csvfile = open('movie_metadata.csv', 'rb') 
#spamreader = csv.reader(csvfile, delimiter=',', quotechar='\n')
spamreader = csv.reader(csvfile)
#next(spamreader,None) # Pula a primeira linha
i = 0 
for row in spamreader:
   total += 1
   if( i == 0):
      print(row[15])
      print(row[25])
      i += 1
   else:
      if( row[15] == '' ):
         count += 1
         continue
      X.append(float(row[15]))
      Y.append(float(row[25]))


print("Total: %d; Vazios: %d; Computados: %d" % (total,count,len(X)))
res = sp(X,Y)
print(res)

exit(0)
if( res == 0):
    print("Não tem correlação!")
else:
    print("Tem Correlação!")





