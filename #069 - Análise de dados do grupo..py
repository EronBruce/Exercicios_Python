
maioridade = 0
totmulher = 0
tothomem = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    resp = ' '
    if idade >= 18:
        maioridade += 1
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
    if sexo == 'M':
        tothomem += 1
    if idade < 20 and sexo == 'F':
        totmulher += 1
    while resp not in 'SN':
        resp = str(input("Quer Continuar? [S/N]:")).upper()
    if resp == 'N':
        break

print('Total de pessoas com mais de 18 anos: {}\n Ao todo temos {} homens cadastrados\n '
      'E temos {} mulheres com menos de 20 anos'.format(maioridade,tothomem,totmulher))
