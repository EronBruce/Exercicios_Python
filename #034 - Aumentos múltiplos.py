salario = float(input('Seu salário : '))
if salario <= 1.250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar {:.2f} agora.'.format(salario, novo))