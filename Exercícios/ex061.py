cont = 0

n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

print('-' * 100)
print('{:^100}'.format('A progressão aritmética é ... '))
print('-' * 100)

while cont < 10:
    if cont == 0:
        print(n1, end=' ')
        cont += 1
    else:
        n1 += r
        print(n1, end=' ')
        cont += 1