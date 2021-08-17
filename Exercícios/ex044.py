valor = float(input('Qual o valor do produto? '))
print('*' * 20)
print('Para escolher a condição de pagamento:')
print('Digite 1 - À vista no dinheiro ou no cheque')
print('Digite 2 - À vista no cartão')
print('Digite 3 - Em até 2x no cartão')
print('Digite 4 - Em 3x ou mais no cartão')
x = int(input('Qual a opção escolhida? '))
print('*' * 20)

if x == 1:
    print('No dinheiro o desconto é de 10% e sua compra foi de R${:.2f} para R${:.2f}.'.format(valor, valor*0.9))
elif x == 2:
    print('No cartão o desconto é de 5% e sua compra foi de R${:.2f} para R${:.2f}.'.format(valor, valor * 0.95))
elif x == 3:
    print('Parcelado em 2x não tem desconto. Valor total R${:.2f}'.format(valor))
elif x == 4:
    print('Em 4x no cartão tem juros de 20%, indo de R${:.2f} para R${:.2f}.'.format(valor, valor*1.2))
else:
    print('\033[1:31mOpção inválida!!')

