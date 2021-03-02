lista = []
maior = 0
menor = 0
for cont in range(0,5):
    lista.append(int(input('Digite um valor para a posição {}:'.format(cont))))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        elif lista[cont] < menor:
            menor = lista[cont]

print(f'vc digitou os valores {lista}')
print(f'o maior valor é o {maior} na posição ', end='')

for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'o menor valor é o {menor} na posição ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
print()