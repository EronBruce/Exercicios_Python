from datetime import date
nasc = int(input('ano de nascimento :'))
atual = date.today().year
idade = atual - nasc

if idade <= 9:
    print('A sua idade é de {} anos'.format(idade))
    print('CATEGORIA MIRIM')
elif idade <= 14:
    print('A sua idade é de {} anos'.format(idade))
    print('CATEGORIA INFANTIL')
elif idade <= 19:
    print('A sua idade é de {} anos'.format(idade))
    print('CATEGORIA JUNIOR')
elif idade <= 25:
    print('A sua idade é de {} anos'.format(idade))
    print('CATEGORIA SÉNIOR')
else:
    print('CATEGORIA MASTER')
