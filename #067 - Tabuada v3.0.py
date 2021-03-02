
while True:
    tabuada = int(input('Tabuada: '))
    if tabuada < 0:
        break
    for c in range(1,11):
        print('{} X {:2} = {}'.format(tabuada,c,tabuada * c))
print('ENCERRADO')
