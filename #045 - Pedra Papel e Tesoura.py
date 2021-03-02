from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0,2)

print(''''Suas opções :
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''''')

jogador = int(input('Qual é a sua jogada?'))

print('\33[31mJO')
sleep(1)
print('\33[32mKEN')
sleep(1)
print('\33[33mPO!!!!!\33[m')
sleep(1)
2

if jogador == 0:
    print('Você jogou PEDRA, o computador jogou {}.'.format(itens[computador]))
elif jogador == 1:
    print('Você jogou PAPEL , o computador jogou {}.'.format(itens[computador]))
elif jogador == 2:
    print('Você jogou PAPEL , o computador jogou {}.'.format(itens[computador]))