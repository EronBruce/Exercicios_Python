resp = 'S'
soma = quant = media = menor = maior = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    # MAIOR E MENOR
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer Continuar? [S/N]: ')).upper().strip()[0]
media = soma / quant
print('vc digitou {} números e a media foi de {}'.format(quant,media))
print('O maior valor foi {} e o menor foi {}'.format(maior,menor))
