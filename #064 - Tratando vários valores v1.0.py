''''n = soma = cont = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    cont = cont + 1
    if n == 999:
        soma - 999
        cont = cont - 1
    else:
        soma = soma + n

print('vc digitou {} números e a soma entre eles foi de {}'.format(cont,soma))
print('\33[32mPROGRAMA FINALIZADO')'''

#Guanabara

n = soma = cont = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número [999 para parar]: '))
print('vc digitou {} números e a soma entre eles foi de {}'.format(cont,soma))
