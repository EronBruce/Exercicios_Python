'''tentativas = 1
from random import randint
computador = randint(0,10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10. \n será que vc consegue adivinhar qual foi?')
palpite = int(input('\33[35mQual seu palpite ?\33[35m'))
while palpite != computador:
    tentativas += 1
    if palpite > computador:
        palpite = int(input('Menos.. tente mais uma vez'))
    if palpite < computador:
        palpite = int(input('Mais.. tente mais uma vez'))
print('\33[32mAcertou\33[32m com {} Tentativas'.format(tentativas))'''

#Guanabara

from random import randint
computador = randint(0,10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10. \n será que vc consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite?'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.. Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
