print('\033[35:1m{:*^100}\033[m'.format(' Mostrar o maior peso num grupo de 5 pessoas '))

menor = 0
maior = 0

for c in range(1,6):
    p = float(input('Qual é o peso da {}º pessoa? '.format(c)))
    if c == 1:
        menor = p
        maior = p
    else:
        if p >= maior:
            maior = p
        if p <= menor:
            menor = p
print('O maior peso é {}kg'.format(maior))
print('O menor pedo é {}kg'.format(menor))