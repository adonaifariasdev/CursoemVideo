'''def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal CursoemVideo.
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


help(contador)'''

'''def somar(a, b, c):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: 
    Função criada por Gustavo Guanabara do canal CursoemVideo.
    """
    s = a + b + c
    print(f'A soma vale {s}.')


somar(3, 2, 5)
# soma(3, 2) #Dara erro pq nao esta informado o tres parametros.'''

'''def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return:
    Função criada por Gustavo Guanabara do canal CursoemVideo.
    """
    s = a + b + c
    print(f'A soma vale {s}.')


somar(3, 2, 5)
somar(3, 2)'''

'''def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return:
    Função criada por Gustavo Guanabara do canal CursoemVideo.
    """
    s = a + b + c
    print(f'A soma vale {s}.')


somar(b=4, c=2) # o a valerá 0, mesmo nao sendo informado.'''

'''# Escopo Global
def teste():
    print(f'Na função teste, n vale {n}')


# Programa Principal
n = 2
print(f'No programa principal, n vale {n}')
teste()'''

# Variavel Global e Local
'''def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa Principal
n = 2
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}') # Dará erro, pois X é uma variavel local.'''

'''def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 global vale {n1}')'''

'''def somar(a=0, b=0, c=0):
    s = a + b + c
    #print(f'A saoma vale {s}') Devo retirar o print e colocar return
    return s


#somar(3, 2, 5) devo colocar uma varivael
resp = somar(3, 2, 5)
print(f'A soma vale {resp}.')
print()
print(somar(3, 2, 5))
print()
r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cáculos deram {r1}, {r2} e {r3}.')'''


# Exercicio como prática

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(fatorial(n))
print(f'O Fatorial de {n} é igual a {fatorial(n)}.')
print()
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f' Os resultados são {f1}, {f2} e {f3}.')
print()
print()


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
print(par(num))
if par(num):
    print('É PAR!')
else:
    print('NÃO É PAR!')
