print('-' * 20)
print('LOJA SUPER BARATÃO')
print('-' * 20)
soma = custo1000 = menor = cont = 0
barato = ' '
while True:
    produtos = str(input('Produto: '))
    preco = float(input('Preço R$:'))
    cont += 1
    soma += preco
    if preco > 1000:
        custo1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produtos
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print("\33[31mO total gasto na loja foi de R${:.2f}".format(soma))
print('\33[32m{} produtos custam mais de R$ 1000'.format(custo1000))
print('\33[33mO nome do produto mais barato é {} e custa R${}'.format(barato, menor))