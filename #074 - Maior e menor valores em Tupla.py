from random import randint
numeros = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')

print('\nO maior valor sorteado foi {}'.format(max(numeros)))
print('O menor valor sorteado foi {}'.format(min(numeros)))
