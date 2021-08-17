print('\033[31:1m{:-^40}\033[m'.format('Desafio da Tabuada'))
t = int(input('Digite o número para ver sua tabuada: '))

for c in range(1, 11):
    print('{} X {:^2} = {}'.format(t, c, t*c))
