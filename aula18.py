# Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
# As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
# acessíveis por chaves individuais.

'''dados =['Pedro', 25]
pessoas = list()
pessoas.append(dados[:]) #Realiza uma cópia de Dados(ou seja, lista dentro de uma outra lista

#declarando tudo de uma vez
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]] #listas dentro de listas
#              0      1       0      1      0      1
#                 0               1             2
#exemplo de comando
print(pessoas[0][0]) #o primeiro indice se relaciona com o 0 da primeira lista
# o segundo indice se relaciona ao 0 da lista que esta dentro da primeira lista
# irá escrever 'Pedro'

#outro exemplo
print(pessoas[1][1]) # irá escrever 19

#outro exemplo
print(pessoas[2][0]) #irá escrever 'João'

#outro exemplo
print(pessoas[1]) # irá escrevr ['Maria', 19] toda lista 1'''

# Parte Prática da Aula 18
'''
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

''''#demostração de mostragem na tela
galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)#mostra todas as listas dentro da listona
print(galera[0]) #mostra o item 0 da listona ['Joao', 19]
print(galera[0][0]) #Neste caso irá mostrar so 'Joao'
print(galera[2][1]) # aqui irá mostrar 13, item 2 da listona da item 1
'''

'''#utilizando o FOR
galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    #print(p[0]) #mostrará apenas os nomes
    #print(p[1]) #mostrará apenas as idades
    print(f'{p[0]} tem {p[1]} anos de idade')'''

# Pedir nome e idade
galera = list() #lista principal
dado = list() #pegar dado temporariamente, lista secundário
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # se tirar [:] irá momstrar listas vazias
    dado.clear() # comando para EXCLUIR DADO
print(galera) # mostrará [['Pedro', 22], ['Maria', 33], ['Joao', 25]]

#se quiser colocar uma condição, exemplo pessoas maiores de 21 anos
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')

