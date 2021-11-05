# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


valor = int(input('Digite o valor que deseja sacar? R$'))
total = valor
cedulas = 50
contCedulas = 0
while True:
    if valor >= cedulas:
        valor -= cedulas
        contCedulas += 1
    else:
        if contCedulas > 0:
            print(f'{contCedulas} cédulas de R${cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        contCedulas = 0
        if valor == 0:
            break
print('FIM DO SAQUE')