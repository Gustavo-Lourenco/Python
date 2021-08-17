n1 = int(input('Digite o número de início: '))
n2 = int(input('Digite o número fnal: '))
print('\033[1mOs números pares entre {} e {} são:\033[m '.format(n1, n2))

for c in range (n1, n2+1):
    if c%2 == 0:
        print(c, end=' ')
