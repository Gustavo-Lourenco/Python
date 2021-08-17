lista = []

for c in range(1, 6):
    n = int(input(f'Digite o {c}º número: '))
    if c == 1:
        lista.append(n)
        print('Número adicionado ao início da lista!')
    if c == 2:
        if n >= lista[0]:
            print('Número adicionado ao final da lista ...')
            lista.append(n)
        else:
            print('Número adicionado ao início da lista!')
            lista.insert(0, n)
    if c == 3:
        if n >= lista[1]:
            print('Número adicionado ao final da lista ...')
            lista.append(n)
        elif lista[0] < n < lista[1]:
            print('Número adicionado na posição 1 da lista ...')
            lista.insert(1, n)
        else:
            print('Número adicionado ao início da lista ...')
            lista.insert(0, n)
    if c == 4:
        if n >= lista[2]:
            print('Número adicionado ao final da lista ...')
            lista.append(n)
        elif lista[1] < n < lista[2]:
            print('Número adicionado na posição 2 da lista ...')
            lista.insert(2, n)
        elif lista[0] < n < lista[1]:
            print('Número adicionado na posição 1 da lista ...')
            lista.insert(1, n)
        else:
            print('Número adicionado ao início da lista ...')
            lista.insert(0, n)
    if c == 5:
        if n >= lista[3]:
            print('Número adicionado ao final da lista ...')
            lista.append(n)
        elif lista[2] < n < lista[3]:
            print('Número adicionado na posição 3 da lista ...')
            lista.insert(3, n)
        elif lista[1] < n < lista[2]:
            print('Número adicionado na posição 2 da lista ...')
            lista.insert(2, n)
        elif lista[0] < n < lista[1]:
            print('Número adicionado na posição 1 da lista ...')
            lista.insert(1, n)
        else:
            print('Número adicionado ao início da lista ...')
            lista.insert(0, n)
print(f'Os valores digitados foram {lista}')