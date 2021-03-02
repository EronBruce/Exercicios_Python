from datetime import date
ano = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\33[32mO ano {} é BISSEXTO\33[32m'.format(ano))
else:
    print('O ano {} \33[31mNÃO É BISSEXTO\33[31m'.format(ano))