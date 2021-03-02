lista = []
while True:
    resp = ' '
    n = int(input('Diite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor add com sucesso...')
    else:
        print('valor duplicado! Não vou add... ')
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N]:')).upper().strip()[0]
    if resp in 'N':
        break
print('-=' * 20)
lista.sort()
print(f'vc digitou os valores {lista}')



