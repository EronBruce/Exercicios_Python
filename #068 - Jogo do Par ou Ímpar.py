from random import randint
print("=-=" * 10)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-=" * 10)
v = 0
while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
         tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print('Vc jogou {} e o computador {}, total de {}'.format(jogador, computador, total), end=' ')
    print('deu PAR' if total % 2 == 0 else 'deu ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Vc VENCEU!')
            v += 1
        else:
            print('vc PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Vc VENCEU!')
            v += 1
        else:
            print('vc PERDEU!')

    print('Vamos jogar novamente...')
print('\33[31mGAME OVER!\33[31m vc venceu {} vezes'.format(v))