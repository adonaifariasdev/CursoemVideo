# Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python.
# Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.
# Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.

#Inicio da Aula 20
'''print('-' * 30)
print('   CURSO EM  VÌDEO   ')
print('-' * 30)
print('-' * 30)
print('   APRENDA PYTHON   ')
print('-' * 30)
print('-' * 30)
print('   GUSTAVO GUANABARA   ')
print('-' * 30)'''

'''def lin():
    print('-' * 30)


#Programa Principal
lin()
print('   CURSO EM  VÌDEO   ')
lin()
print('   APRENDA PYTHON   ')
lin()
print('   GUSTAVO GUANABARA   ')
lin()'''

'''
def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' *30)


#Programa Principal
titulo('     CURSO EM VÍDEO     ')
titulo('     APRENDA PYTHON     ')
titulo('     GUSTAVO GUANABARA     ')

# Fim da Aula 20
'''

# Inicio da Pràtica da Aula 20
'''
a = 4
b = 5
s = a + b
print(s)
#soma(4, 5) ----> Pode ser criada essa função!

a = 8
b = 9
s = a + b
print(s)
#soma(8, 9) ----> Pode ser criada essa função!

a = 2
b = 1
s = a + b
print(s)
#soma(2, 1) ----> Pode ser criada essa função!
print()

def soma(a, b): # Função recebendo 2 parametros
    s = a + b
    print(s)


# Programa Principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
print()
soma(a=4, b=5)

print()
'''

'''
def soma(a, b): # Função recebendo 2 parametros
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa Principal
soma(4, 5)
print()
soma(b=4, a=5)
print()
soma(7, 2)
'''
#EMPACOTAMENTO
'''
def contador(* num):
    print(num)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''
print()
'''
def contador1(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')


contador1(2, 1, 7)
contador1(8, 0)
contador1(4, 4, 7, 6, 2)
'''

'''
def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''

'''
# Trabalhando com Listas (Funções Parte 1)
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [7, 2, 5, 0, 4]
print(valores)
dobra(valores)
print(valores)
'''


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)