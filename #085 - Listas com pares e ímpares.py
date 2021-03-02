lista = [[], []]
for c in range(1, 8):
    n = int(input('Digite o {}° valor: '.format(c)))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram {lista[0]}')
print(f'E valores ímpares digitados foram {lista[1]}')
