import numpy as np

dataset=np.loadtxt('paises.csv',delimiter=';',dtype=str,encoding='utf-8')

#01 - mostrar pais, regiao, populacao e area

print(dataset[0,:])
print(dataset[0:,0:4])

#02 - contar e Mostrar as diferentes regioes

reg_unica=(np.unique(dataset[1:,1]))

print("Total de regiões diferentes: {}".format(len(reg_unica)))

print("Regiões: {}".format(reg_unica))


#03

media_alfa = (dataset[1:,9].astype(float)).mean()
print("Média de alfabetização: {:.2f}\n".format(media_alfa))

#04 - Quantos Paises sao da America do Norte

mask_north_america = np.char.strip(dataset[:, 1]) == 'NORTHERN AMERICA'

paises_north_america = np.unique(dataset[mask_north_america, 0])

print(f"Países da América do Norte: {len(paises_north_america)}")

#05

import numpy as np

dataset=np.loadtxt('paises.csv',delimiter=';',dtype=str,encoding='utf-8')

mask = np.char.strip(dataset[:, 1]) == 'LATIN AMER. & CARIB'
america_sul_caribe = dataset[mask]
posicao = np.argmax(america_sul_caribe[:, 8].astype(float))
pais = america_sul_caribe[posicao, 0]
gdp = america_sul_caribe[posicao, 8]

print(f"País com maior GDP per capita: {pais}")
print(f"GDP per capita: {gdp}")
