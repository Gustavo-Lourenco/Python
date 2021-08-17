soma = 1

print('-' * 100)
print('{:^100}'.format('Desafio cálculo do fatorial!!'))
print('-' * 100)

n = int(input('Digite um número: '))
counter = n - 1

'''for c in range(n-1, 0, -1):
    if c == n-1:
        soma = n*c
    else:
        soma = soma*c'''

while 1 < counter:

    if counter == n - 1:
        soma = counter * n
        counter = counter - 1

    else:
        soma = soma*counter
        counter = counter - 1

print('{} Fatorado é: {}'.format(n, soma))