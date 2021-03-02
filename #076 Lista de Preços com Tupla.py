listagem = ('Lápis',1.75,
            'Borracha', 2,
            'Caderno',15.90,
            'Estojo',25,
            'Transferidor',4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas',22.30,
            'Livro', 34.90)
print('-' * 40)
print('LISTAGEM DE PREÇOS')
print('-' * 40)
for itens in range(0, len(listagem)):
    if itens % 2 == 0:
        print(f'{listagem[itens]:.<30}', end='')
    else:
        print(f'R${listagem[itens]:>7.2f}')
print('-' * 40)