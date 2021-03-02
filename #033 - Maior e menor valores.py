a= int(input('Primeiro Valor: '))
b= int(input('Segundo Valor: '))
c= int(input('Terceiro Valor: '))

# verificando quem é menor

menor  = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# verificando quem é maior

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('\33[31mO menor valor digitado foi {}'.format(menor))
print('\33[32mO maior valor digitado foi {}'.format(maior))