
while True:
    print('-' * 100)
    n = int(input('Digite um número para mostrar a sua tabuada: '))
    print('-' * 100)
    if n < 0:
        break
    else:
        for c in range (1, 10):
            print(f'{n} X {c} = {n*c}')
print('Programa finalizado!!!')