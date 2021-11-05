'''for c in range(1, 10):
    print(c)
print('FIM')'''

'''c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')'''

'''n = 1
while n != 0: #flag ou condição de parada
    n = int(input('Digite um valor: '))
print('FIM')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('FIM')'''

n = 1
totPar = totaImpar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: # nao vai contabilizar o 0 no final da contagem
        if n % 2 ==0:
            totPar += 1
        else:
            totaImpar += 1
print('Você digitou {} numeros pares e {} numeros impares.'.format(totPar, totaImpar))
# OBS.: nesse caso não vai considerar o 0 como numero!!!!
