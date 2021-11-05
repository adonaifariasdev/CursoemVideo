'''lanche = 'Hamburguer'
lanche = 'Suco'
print('NA VARIAVEL SIMPLES: ')
print(lanche) #Observe que ele mostrará o 'Suco', pois o 'Hamburguer' foi substituído pelo outro.
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim' )
print('NA TUPLA: ')
print(lanche)'''

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita') # Com parênteses
print(lanche)
#lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim' # Sem parênteses
print(lanche) # 0         1       2        3 = 4 elementos
#              -4        -3      -2       -1
print(lanche[1]) # Observe que na hora de referenciar, sempre se utilizará colchetes. Nesse caso mostrará o Suco.
print(lanche[3])
print(lanche[-2])
print(lanche[1:3]) # Na hora do fatiamento o elemento 3 é ignorado
print(lanche[2:]) # vai do elemnto 2 até o final, nesse caso da Pizza até o Pudim
print(lanche[:2]) # vai do início até o elemento 2, mostrará Hamburguer e o  Suco
print(lanche[-2:]) # vai começar na Pizza e vai até o final, ou seja, Pudim
# Tuplas são imutáveis
#lanche[1] = 'Refrigerante' # Confome dito abaixo, esse comando está ERRADO!
print(lanche[1]) # mostrará erro, pois o lanche[1] não pode ter item atribuído, com exceção na sua declaração.
print(lanche)

#Outra fomra com F print
for comida in lanche: #Nessa caso estou utilizando o FOR como Itens, sem o RANGE
    print(f'Eu vou comer {comida}') # Irá mostrar cada comida da Tupla, pois "comida" nesse caso está no FOR como iteração
print('Comi pra caramba!')
print(len(lanche))
print('Comi pra caramba!')

for cont in range(0, len(lanche)):
    #print(cont) # Se fizer esse comando irá aparecer 0 1 2 3 4
    #print(lanche[cont]) # Ai irá aparecer Hamburguer Suco Pizza Pudim Batata Frita
    print(f'Eu vou comer {lanche[cont]} na posição {cont}') # outra forma de mostrar os itens.

for pos, comida in enumerate(lanche):# O comando enumerate mostra tanto o dado quanto a posição
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche)) #O comando sorted quer dizer "EM ORDEM" ou "ORGANIZADO" mostrando em Ordem Alfabetica.
# OBS acima que ele não muda a TUPLA, somente organiza  a ordem, tanto q no comando abaixo ainda continua como estava.
print(lanche)
print('-='*40)
print('-='*40)

a = (3, 5, 4)
b = (5, 8, 1, 2)
c = a + b # juntará uma TUPLA na ouutra
print(a)
print(b)
print(c)# ira mostrar (2, 5, 4, 8, 1, 2) -- Se c = b + a -> mostrará (5, 8, 1, 2, 3, 5, 4), ou seja, a ordem influencia
print(len(c)) #irá mostrar resultado 7
print(c.count(5)) # irá mostrar quantas vezes o número 5 está aparecendo dentro da Tupla C

print(c)
print(c.index(8)) # mostrará o index de 8, resultando num 4. Ou seja, qual posição está o 8.
print(c.index(4))
print(c.index(2, 4)) # chamamos isso de deslocamento.
print('-='*40)
print('-='*40)

pessoa = ('Gustavo', 39, 'M', 99.88) #dentro das minhas TUPLAS posso ter dados de tipos diferentes.
#del(pessoa) # ele irá apagar da memoria, ai dará Traceback, nem mesmo se colocar del(pessoa[0])
print(pessoa)


