cont = 0
lista = []

while True:
    n = int(input('Digite um número: '))
    cont += 1
    lista.append(n)
    while True: # Verifica a condição da continuação
        s = str(input('Você deseja continuar? [S/N] ')).upper().strip()[0]
        if s in 'SN':
            break
        else:
            print('Opção inválida, tente novamente.', end=' ')
    if s == 'N':
        break
print(f'Foram digitados {cont} números no total')
print(f'Os números em ordem decrescente são: {sorted(lista, reverse=True)}')

if lista.count(5) != 0:
    print(f'O 5 faz parte da lista e está nas posições: ', end='')
    for c in range(0, len(lista)):
        if lista[c] == 5:
            print(c, end=' ')
else:
    print('O 5 não faz parte da lista')

