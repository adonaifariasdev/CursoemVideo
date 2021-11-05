# Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python.
# Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.

'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas) # Mostra {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
#print(pessoas[0]) #Dará ERRO
print(pessoas['nome']) #Mostra o nome
print(pessoas['idade']) #Mostra a idade
# print(f'O {pessoas['nome']} tem {pessoas['idade']} anos') #Dará ERRO
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') #Usar com aspas duplas

print(pessoas.keys()) #Mostra as chaves dict_keys(['nome', 'sexo', 'idade'])
print(pessoas.values()) #Mostra os valores dict_values(['Gustavo', 'M', 22])
print(pessoas.items()) # Mostra dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])
# Disse que os items são uma lista e é composta de 3 tuplas
print()

#Acessando por LAÇOS
for k in pessoas.keys():
    print(k) #mostrara as chaves nome, sexo, idade -> As chaves
print()

for k in pessoas.values():
    print(k) #Mostrara os valores Gustavo, M, 22
print()

for k in pessoas.items():
    print(k) #Mostrará chaves e valores
print()

for k, v in pessoas.items():
    print(f'{k} = {v}') #Mostra noome = Gustavo / sexo = M / idade = 22
print()
#OBS no dicionario nao tem enumerate'''

'''#Apagando uma chave
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
del pessoas['sexo'] #Apagará o elemento sexo
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()

#Modificando o valor
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['nome'] = 'Leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()

#Adicionando o valor
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['peso'] = 98.5 #Não precisa de Append
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()'''

'''# Criando um DICIONÁRIO dentro de uma LISTA
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1) #Mostrara {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
print(estado2) #Mostrara {'uf': 'São Paulo', 'sigla': 'SP'}
print()
print(brasil) #Mostrará [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]
# Uma LISTA com DICIONÁRIOS dentro
print()
print(brasil[0]) #Mostra {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
print(brasil[1]) #Mostra {'uf': 'São Paulo', 'sigla': 'SP'}
print(brasil[0]['uf']) #Mostra Rio de Janeiro
print(brasil[1]['sigla']) #Mostra SP'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    #brasil.append(estado) #Nao sera possivel
    #brasil.append(estado[:])  #Dará ERRO
    brasil.append(estado.copy()) #Forma correta da fazer a cópia
print(brasil)
print()

#Mostrando cada estado
for e in brasil:
    print(e)
print()


for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
print()

#Somente pros valores
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()