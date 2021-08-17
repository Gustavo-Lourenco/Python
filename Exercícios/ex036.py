print('*' * 20)
print('Olá Sr(a), seja muito bem vindo(a) ao nosso banco: ')
casa = float(input('Qual o valor da casa?: '))
salario = float(input('Qual o valor do seu salário?: '))
tempo = float(input('Em quantos anos a casa será paga?: '))

mensal = ((casa / tempo) / 12)

print('O valor da mensalidade para o tempo de {:.0f} anos é de R${:.2f}'.format(tempo, mensal))
print('*' * 20)

if salario*0.3 >= mensal:
    print('O empréstimo está aprovado pois o valor é menor que 30% do seu salário')
else:
    print('\033[31mO empréstimo está reprovado pois o valor excede 30% do seu salário')

