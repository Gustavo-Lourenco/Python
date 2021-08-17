print('\033[31:1m{:=^60}\033[m'.format(' Cálculo de uma Progressão Aritmética '))
ni = int(input('Digite o 1º termo da PA: '))
r = int(input('Digite a razão da PA: '))
counter = 0

for c in range(ni, ni*11, r):
    counter = counter + 1
    print('O {}º termo da PA é: {}'.format(counter, c))



