print('*' * 100)
print('{:^100}'.format('Digite quantos números da sequência Fibonacci você quer ver'))
print('*' * 100)

fibonacci = 0
cont = 0
v1 = 0
v2 = 1

n = int(input('Digite a quantidade de elementos da série Fibonacci: '))
print(v1, end=' ')
print(v2, end=' ')

while cont < n - 2:
    if cont % 2 == 0 and cont == 0:
        fibonacci = v1 + v2
        print(fibonacci, end=' ')
        v1 = fibonacci
        cont += 1
    else:
        if cont % 2 == 0:  # vermelho
            fibonacci = fibonacci + v1
            print('{}'.format(fibonacci), end=' ')
            v1 = fibonacci
            cont += 1
        if cont % 2 == 1:  # Azul
            fibonacci = fibonacci + v2
            print('{}'.format(fibonacci), end=' ')
            v2 = fibonacci
            cont += 1
