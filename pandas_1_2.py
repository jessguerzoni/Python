import numpy as np
import pandas as pd

#01
seriesAno1=pd.Series({'Java': 16.25, 'C': 16.04, 'Python':9.85})
seriesAno2=pd.Series({'C':16.21,'Python':12.12,'Java':11.68})

print(seriesAno1)
print(seriesAno2)

#2
v1=seriesAno1.sum()
v2=seriesAno2.sum()

print('Porcentagem total:')
print(v1, '%')
print(v2, '%')

#3 
alteracao = seriesAno2 - seriesAno1
print('Alteração nos resultados:')
print(alteracao)

#4 
cresc = alteracao[alteracao > 0]

print('Crescimento:')
print(cresc)

#5 
projecao = seriesAno2 + alteracao * 2

print('Projeção daqui a 2 anos:')
print(projecao)

print('Linguagem mais popular:')
print(projecao.nlargest(1))

np.random.seed(10)
df = pd.DataFrame(
    data=np.random.randint(1, 50, [5, 4]),
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z'])

print(df)

#6 
media_x = df.loc[df['X'] < 30, 'X'].mean()
print('Média dos valores de X menores que 30:', media_x)

#7 
media_d = df.loc['D'].mean()
soma_e = df.iloc[4].sum()   

print('Média da linha D:', media_d)
print('Soma da linha E:', soma_e)

#8 
fatia = df.loc[['A', 'C', 'E'], ['X', 'Y']]
print(fatia)

print('Soma de cada linha:')
print(fatia.sum(axis=1).to_string())

print('Soma de cada coluna:')
print(fatia.sum(axis=0).to_string())
