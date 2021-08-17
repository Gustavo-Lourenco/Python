n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 == n2:
    print('\033[31:1mOs números são iguais!!!')
elif n1 < n2:
    print('O primeiro valor é o menor número')
else:
    print('O segundo valor é o menor número')
