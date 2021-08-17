print('Teste de verificação de números primos: ')
n = int(input('Digite um número: '))
counter = 0

for c in range(1, n+1):
    if n%c == 0:
        counter = counter + 1
        print('\033[31m{}\033[m'.format(c), end=' ')
    else:
        print('\033[33m{}\033[m'.format(c), end=' ')

if counter != 2:
    print('\nO número digitado não é PRIMO')
else:
    print('\nO número digitado é PRIMO!!!!')