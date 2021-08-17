listagem = ('Celular', 2500, 'Notebook', 4000, 'Televisão', 4500, 'Geladeira', 5000, 'Mouse', 10.90)
d = 0
print('-' * 50)
print('{:^50}'.format('Listagem de preços'))
print('-' * 50)

for c in range(0, len(listagem)-5):
    print('{:.<40}'.format(listagem[d]), end='')
    d += 1
    print('R${:>8.2f}'.format(listagem[d]))
    d += 1
print('-' * 50)