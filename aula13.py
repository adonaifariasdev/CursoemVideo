'''for c in range(0, 10, 2):
    print(c)
print('FIM')'''

'''n = int(input('Digite um número: '))
for c in range(0, n+1):
    print('{}'.format(c), end=', ')
print('FIM')'''

'''i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print('{}'.format(c), end=', ')
print('FIM')'''

soma = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    soma = soma + n # s += n
print('SOMA: {}'.format(soma))
print('FIM')