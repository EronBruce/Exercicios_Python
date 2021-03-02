n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

if media >= 7.0:
    print('sua média é de {}'.format(media))
    print('\33[32mAPROVADO!!!!')
elif 7 > media >= 5:
    print('sua média é de {}'.format(media))
    print('\33[36mRECUPERAÇÃO...')
else:
    print('sua média é de {}'.format(media))
    print('\33[31mREPROVADO!!!')
