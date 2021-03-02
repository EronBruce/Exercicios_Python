distancia = float(input('Qual é a distancia da sua viagem?  '))
if distancia <= 200:
    passagem = distancia * 0.50
    print('Você está prestes a viajar \33[35m{:.0f}km\33[m'.format(distancia))
    print('O valor da sua passagem é de R${:.2f}'.format(passagem))
else:
    if distancia > 200:
        passagem = distancia * 0.45
        print('Você está prestes a viajar \33[33m{}km\33[m'.format(distancia))
        print('O valor da sua passagem é de R${:.2f}'.format(passagem))
print("\33[1;34mBoa viagem!")