lista = []

for c in range(1, 6):
    n = int(input('Digite um número: '))
    lista.append(n)
    #lista.append(int(input('Digite um número: ')))
print(f'Você digitou os valores : {lista}')
print(f'O maior valor digitado foi {max(lista)} e ele estava na posição:', end=' ')
for d in range(0, 5):
    if lista[d] == max(lista):
        print(f'{d+1}...', end=' ')
print(f'\nO menor valor digitado foi {min(lista)} e ele estava na posição:', end=' ')
for e in range(0, 5):
    if lista[e] == min(lista):
        print(f'{e+1}...', end=' ')
