from datetime import date
atual = date.today().year
menor = 0
maior = 0
for c in range(1,8):
    nasc = int(input('Ano de nascimento da {}° pessoa: '.format(c)))
    idade = atual - nasc
    if idade >= 18:
        maior = maior + 1

    if idade < 18:
        menor = menor + 1

print('Ao todo tivemos \33[31m{} maiores de idade \n e \33[32m{} menores de idade'.format(maior, menor))



