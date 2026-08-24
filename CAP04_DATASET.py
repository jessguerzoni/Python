#01

import numpy as np
import math
dataset=np.loadtxt('space.csv',delimiter=';',dtype=str,encoding='utf-8')

print(dataset[0,:])
status = dataset[:,7]

success=np.sum(dataset[:,7]=='Success')
porcent=success/len(status)*100
print('Porcentagem: {:.2f}'.format(porcent))

#02

gasto = dataset[1:, 6].astype(float) 

cost = gasto[gasto>0]
media=np.mean(cost)

print(f"Média dos gastos: {media:.2f}")

#03

#quantas missoes foram realizadas pelos EUA

eua=dataset[np.char.find(dataset[:,2],'USA')>=0] #:=todas as linhas, 2 - coluna 2
tot_eua=[len(eua)] #quantas vezes EUA aparece
print(tot_eua)

#04

#Missao mais cara da SpaceX

spacex=dataset[np.char.find(dataset[:,1],'SpaceX')>=0]
gasto=spacex[:,6].astype(float) #associa a relacao das colunas com spaceX e converte os valores da coluna cost em float
maior=np.max(gasto)
print('Maior gasto: {}'.format(maior))

#05

empresa=np.unique(dataset[1:,1],return_counts=True)

for i in range(len(empresa[0])):
    print("Empresa: {}".format(empresa[0][i]))
    print("Numero de missao: {}".format(empresa[1][i]))

#06

status_rocket = dataset[1:, 5]
quantidade_retired = np.sum(status_rocket == "StatusRetired")
porcentagem = (quantidade_retired / len(status_rocket)) * 100
print("Porcentagem de missões: {:.2f}%".format(porcentagem))

#07

localizacoes = dataset[1:, 2]
localizacoes_russia = np.char.find(localizacoes, "Russia") >= 0
quantidade = np.sum(localizacoes_russia)
print("Quantidade de missões lançadas da Russia:", quantidade)

#08
custos = dataset[1:, 6]
indice = np.argmax(custos)
empresa = dataset[1:, 1][indice]
valor = custos[indice]
print("Empresa:", empresa)
print("Valor da missão:", valor)
