while True:
    n = str(input('Digite uma expressão: '))
    abre = n.count('(')
    fecha = n.count(')')
    if abre == fecha:
        print('Condição 1 - OK')
        if n.index('(') < n.index(')'):
            print('Condição 2 - OK')
            if n.rindex(')') > n.rindex('('):
                print('Condição 3 - OK')
                #print(n.rindex(')'))
                #print(n.rindex('('))
                print('A expressão é Válida!')
            else:
                print('A expressão é inválida!')
        else:
            print('A expressão é inválida!')
    else:
        print('A expressão é inválida!')
