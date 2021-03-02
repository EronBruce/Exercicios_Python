print('-=-' * 20)
print("                LOJA DE COMPRAS BRUCE")
print('-=-' * 20)
compra = float(input('Preço das compras: R$'))


print('''    FORMAS DE PAGAMENTO
    [ 1 ] à vista dinheiro/cheque
    [ 2 ] à vista cartão
    [ 3 ] 2x no cartão
    [ 4 ] 3x ou mais no cartão''')

opcao = int(input('Qual é a sua opção? '))
if opcao == 1:
    desconto = compra - (compra * 10 / 100)
    print('sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(compra, desconto))
elif opcao ==2:
    desconto = compra - (compra * 5 / 100)
    print('sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(compra, desconto))
elif opcao == 3:
    print('seu preço final é de {:.2f}.'.format(compra))
elif opcao == 4:
    parcela = int(input('Quantas parcelas deseja? '))
    juros = compra + (compra * 20 / 100)
    print('sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(compra, juros))
    print('juros de {:.2f}.'.format(juros / parcela))





