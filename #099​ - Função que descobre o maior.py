from time import sleep

def contador(* núm):
    cont = maior = 0
    print('-=' * 30)
    print('\nAnalisando os valores passados...')
    for valor in núm:
        print(f'{valor}', end=' ',flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram imformados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')





contador(2,9,4,5,7,1)
contador(4,7,0)