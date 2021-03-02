lista = []
while True:
    n = lista.append(int(input("Digite um número : ")))
    resp = str(input("Quer Continuar ? [S/N]")).upper().strip()[0]
    if resp in "N":
        print('Programa encerrado..')
        break

print('vc digitou', len(lista), 'elementos.')
lista.sort(reverse=True)
print('Os valores em ordem decrescente são', lista)
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print("O valor 5, não faz parte da lista")
