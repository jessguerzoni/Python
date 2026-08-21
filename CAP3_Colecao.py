#1

#criando a lista vazia
lista=[]

#acrescentando elementos na lista

for i in range(5):
  lista.append(input("Digite o nome do time: "))

#a)
print("Os três primeiros colocados: {} ".format(lista[0:3]))

#b)
print("Os dois ultimos colocados: {}".format(lista[-2:]))

#c)
print("Ordem alfabética: {}".format(sorted(lista)))

#d)
if "Barcelona" in lista:
  print("Barcelona se encontra da posicao de índice {}".format(lista.index("Barcelona")))
else:
  print("Barcelona não está na lista")


#2


loja1={'SamsungA9','Iphone17','Xiaomi Redmi 14','Motorola S10'}
loja2={'Siemens A50','Nokia 3310','Sony Ericsson W300','Motorola V3'}


print("Itens da loja 01: {}".format(loja1))
print("Itens da loja 02: {}".format(loja2))

#modelos disponíveis em ambas

ambas=loja1&loja2

if ambas:

  print("Modelos disponíveis em ambas as lojas: {}".format(ambas))
else:
  print("Não há modelos em comum para ambas as lojas")

#modelos no total
total=loja1|loja2
print("Modelos disponíveis em ambas as lojas: {}".format(total))

#3


dicionario = {}

dicionario['nome'] = input("Digite o nome do aluno: ")
dicionario['media'] = float(input("Digite a média do aluno: "))

#Verificação da média
if dicionario['media'] >= 50:
    dicionario['Situação: '] = 'AP'
else:
    dicionario['Situação: '] = 'RP'

#Dicionario completo

print(dicionario)

#4

tup = []

for i in range(3):
    nome = input("Digite um nome: ")
    peso = float(input("Digite o peso: "))
    tup.append((nome, peso))

pesada = tup[0]
leve = tup[0]

for pessoa in tup:
    if pessoa[1] > pesada[1]:
        pesada = pessoa
    if pessoa[1] < leve[1]:
        leve = pessoa

print(f"Pessoa mais pesada: {pesada[0]} ({pesada[1]} kg)")
print(f"Pessoa mais leve: {leve[0]} ({leve[1]} kg)")

#5

qtde = int(input("Digite quantas pessoas: "))
lista = []

for i in range(qtde):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo: ")
    lista.append((nome, idade, sexo)) 

#media
soma_id = 0
for i in lista:
    soma_id = soma_id+i[1]  #i[1] é a idade vinda do append (i[0] - nome, i[1]-idade, i[2]-sexo)

media = soma_id / qtde

#<20
menos20 = 0
for i in lista:
    if i[2].upper() == "F" and i[1] < 20:
        menos20 = menos20 + 1

print(f"Média de idade do grupo: {media:.2f}")
print(f"Quantidade de mulheres com menos de 20 anos: {menos20}")

#6
receita=['ovo','farinha','leite','fermento']

#adicionando ingredientes

ing_novo=input('Qual ingrediente deseja acrescentar: ')
receita.append(ing_novo)

#inserindo em posição especifica

posicao=int(input('Em qual posição deseja acrescentar o ingrediente: '))
receita.insert(posicao,'açúcar')

#removendo ingrediente pelo valor

receita.remove('leite')

print(receita)

#7

receita=['ovo','farinha','leite','fermento','chocolate']

# Transformando lista em conjunto
receita_conj = set(receita)

# Ingredientes que cada pessoa tem em casa
p1 = {'ovo', 'farinha','chocolate'}
p2 = {'leite', 'fermento', 'açúcar'}

# Ingredientes que faltam para cada pessoa
fp1 = receita_conj - p1
fp2 = receita_conj - p2

print(f"Ingredientes faltantes para a pessoa 1: {fp1}")
print(f"Ingredientes faltantes para a pessoa 2: {fp2}")


#8

produtos = []

for i in range(3):
  
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade[estoque]: "))
    
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    
    produtos.append(produto)


for produto in produtos:  #percorre lista para mostrar o valor final

    valor_total = produto["preco"] * produto["quantidade"]
    print(f"{produto['nome']}: R$ {valor_total:.2f}")


