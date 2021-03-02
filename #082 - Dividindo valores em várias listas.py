lista = []
pares = []
impares = []
while True:
    n = lista.append(int(input("Digite um número : ")))
    resp = str(input('Quer Continuar ? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('=-' * 30)
lista.sort()
print('A lista completa é', lista)
print('A lista de pares é', pares)
print('A lista de impares é', impares)
