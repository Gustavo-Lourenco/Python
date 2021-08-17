s = float(input('Qual o valor do seu salário? '))

if s>1250:
    print('O valor do seu novo salário é R${:.2f}'.format(s*1.1))
else:
    print('O valor do seu novo salário é R${:.2f}'.format(s*1.15))
