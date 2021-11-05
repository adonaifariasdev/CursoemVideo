from random import randint
from time import sleep
from os import system
opcao = 's'
contPC = 0
contUS = 0
while opcao != 'N':

    print('='*40)
    print('{:=^40}'.format(' JO KEN PO 2.0 '))
    print('{:=^40}'.format(' Ceated By: Ten Adonai '))
    print('         JOGADOR {} x {} COMPUTADOR'.format(contUS, contPC))
    print('='*40)
    print('''Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')
    itens = ('PEDRA', 'PAPEL', 'TESOURA')
    #print(itens)
    jogador = int(input('Qual a sua jogada? '))
    computador = randint(0, 2)
    sleep(0.5)
    print('JO..')
    sleep(0.5)
    print('KEN..')
    sleep(0.5)
    print('PO..')
    print(' {:=^40} '.format(' JO KEN PO '))
    print('|{:^40}|'.format('RESULTADOS'))
    print(' {:^40} '.format('-'*40))
    print('           Jogador jogou {}'.format(itens[jogador]))
    print('        Computador jogou {}'.format(itens[computador]))
    print(' {:^40} '.format('-'*40))

    if jogador == 0:

       if computador == 0:
           print('                 EMPATE!!!')
       elif computador == 1:
           print('          COMPUTADOR VENCEU!!!')
           contPC = contPC + 1

       elif computador == 2:
           print('          JOGADOR VENCEU!!!')
           contUS = contUS + 1

    elif jogador == 1:
        if computador == 0:
            print('          JOGADOR VENCEU!!!')
            contUS = contUS + 1

        elif computador == 1:
            print('                 EMPATE!!!')

        elif computador == 2:
            print('          COMPUTADOR VENCEU!!!')
            contPC = contPC + 1

    elif jogador == 2:
        if computador == 0:
            print('          COMPUTADOR VENCEU!!!')
            contPC = contPC + 1

        elif computador == 1:
            print('          JOGADOR VENCEU!!!')
            contUS = contUS + 1

        elif computador == 2:
            print('                 EMPATE!!!')


    else:
        print('JOGADA INVÁLIDA! TENTE NOVAMENTE!')
    print(' {:^40} '.format('='*40))

    print('|{:^40}|'.format('PLACAR ELETRÔNICO'))
    print(' {:^40} '.format('-' * 40))
    print('         JOGADOR {} x {} COMPUTADOR'.format(contUS, contPC))
    print(' {:^40} '.format('-' * 40))

    opcao = str(input('CONTINUAR? [S/N]')).upper()
    if opcao == 'N':
        print('PROCESSANDO...')
        sleep(2)
        print('SAINDO...')
        sleep(1)
        print(' {:^40} '.format('-' * 40))
        print('|{:^40}|'.format('PLACAR ELETRÔNICO'))
        print(' {:^40} '.format('-' * 40))
        print('         JOGADOR {} x {} COMPUTADOR'.format(contUS, contPC))
        print(' {:^40} '.format('-' * 40))
        print(' {:^40} '.format('='*40))

        print('{:^40}'.format('MUITO OBRIGADO POR JOGAR!'))
        print('{:^40}'.format('VOLTE SEMPRE!'))
        print('{:^40}'.format('by: TEN ADONAI'))
        print('{:^40}'.format('contact: oficialadonai@hotmail.com'))
        print(' {:^40} '.format('='*40))
        sleep(3)
    system('cls')