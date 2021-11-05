
'''while True:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')'''

'''n = 0
while n != 999:
    n = int(input('Digite um número:'))'''

# limitara a fazer 3 vezes
'''n = cont = 0
while cont < 3:
    n = int(input('Digite um número:'))
    cont += 1'''

# Se não quiser dizer quantos números são:
'''n = 0
while n != 999: # 999 é o flag, ou seja, o ponto de parada
    n = int(input('Digite um número:'))'''

# Nesse caso, tem que diminuir o 999 da soma para poder somar sem o flag
'''n = s = 0
while n != 999:
    n = int(input('Digite um número:'))
    s += n
print('A soma vale {}'.format(s))'''

# nesse caso a soma mesmo digitando 999 nao sera somado, pois vai dar break e sair
n = s = 0
while True:
    n = int(input('Digite um número:'))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))
# print(f'A soma vale {s}') # modo do Pyhton Antigo'''

# exemplos fom F Strings
nome = 'José'
idade = 33
salario = 987.35
print(f'O {nome} tem {idade} anos.') #Python 3.6+
print('O {} tem {} anos.'.format(nome, idade)) # Modo novo de utilizar as strings # Python 3
print('O %s tem %d anos.' % (nome, idade)) # Utilizado no Python 2
print(f'O {nome} tem {idade} anos e ganha R${salario}') # ESSE MODO SERÁ UTILIZADO NOS PROXIMOS TB
print(f'O {nome:-^20} tem {idade} anos e ganha R${salario:.2f}') # todas as formatações funcionam.