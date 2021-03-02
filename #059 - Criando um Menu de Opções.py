from time import sleep
n1 = int(input('primeiro valor: '))
n2 = int(input('Segundo Valor: '))

opcao = 0
while opcao != 5:
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('>>>>> Qual é a sua opção?'))

    if opcao == 1:
        print('A soma de {} + {} é de {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('Multiplicação de {} X {} é de {}'.format(n1, n2, n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print('O maior número é o {}'.format(n1))
        else:
            print('O maior número é o {}'.format(n2))
    elif opcao == 4:
        n1 = int(input('primeiro novo valor: '))
        n2 = int(input('Segundo novo Valor: '))

    elif opcao == 5:
        print('Finalizando...')
        sleep(3)
    else:
        print('Opção inválida. Tente novamente!')
    print("=-=" * 10)

print('\33[31mPrograma encerrado\33[31m')
