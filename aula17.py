# Observe abaixo que a TUPLA é IMUTÁVEL!!!
'''num = (2, 5, 9,1)
num[2] = 3
print(num)'''

#Já na LISTA os valores do eslementos podem ser trocados, conforme abaixo:
'''num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)'''

''''# Adicionando valores e colocando na Ordem:
num = [2, 5, 9, 1]
print(num)
num[2] = 3 # Substitui o valor do elemento por esse novo, no caso o valor 9 passará a ser 3.
#num[4] = 7 Não pode ser adicionado valores dessa forma, vai dar Traceback, pois a lista so tem 4 elementos indo de 0, 1, 2, 3
num.append(7) #Dessa forma sim será adicionado o 7
print(num)
num.sort() # Colocará na ordem
print(num)
num.sort(reverse=True) # Colocará em Ordem REVERSA
print(num)
print(f'Essa lista tem {len(num)} elementos') # o len mostra quantos elementos tem na lista
num.insert(2, 0) # na posição 2, irá colocar o 0 e aumentará a LISTA
print(num)
print(f'Essa lista tem {len(num)} elementos')

# Remoção de elementos:
num.pop() # Sem nenhum parametro irá eliminar o ultimo elemento da LISTA.
print(num)
num.pop(2) # eliminará o elemento 2 da LISTA
print(num)
num.insert(2, 2)
print(num)
num.remove(2) #Irá remover o primeiro elemento 2, procura o inicio da lista
print(num)
#num.remove(4) # o valor não está na lista, dara ero ao executar
if 4 in num: #Bastante útil
    num.remove(4)
else:
    print('Não achei o número 4')'''


'''valores = [] # pode ser valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
#print(valores)
for v in valores: #mostrará os valores formatados -> para cada valor dentro de valores, imprima...
    print(f'{v}...', end='')
print('\n')
for c, v in enumerate(valores): # Na posição da chave(c), mostra o valor(v) dentro de valores
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
print('\n')
for cont in range(0, 5):
    valores.append((int(input('Digite um valor: '))))
#for c, v in enumerate(valores): # Na posição da chave(c), mostra o valor(v) dentro de valores
#    print(f'Na posição {c} encontrei o valor {v}!')'''

a = [2, 3, 4, 7]
b = a # Observe que para fazer a cópia de a para b deve ser usado da seguinte forma b = a[:], ou seja, cira uma cópia de a para b
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b[2] = 8 #Mudará nas duas listas abaixo: pois é feito uma ligação
print(f'Lista A: {a}')
print(f'Lista B: {b}')

