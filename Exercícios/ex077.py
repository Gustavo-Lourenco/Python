dicionario = ('hipotenusa', 'estoico', 'incautos', 'convalescencia', 'estirpe', 'outrora', 'regicida', 'incipiente')

for d in range(0, len(dicionario)):
    print(f'\nNa palavra \033[1m{dicionario[d]}\033[m temos as vogais: ', end='')
    for c in range(0, len(dicionario[d])):
        if dicionario[d][c] in 'aeiou':
            print(dicionario[d][c], end=' ')