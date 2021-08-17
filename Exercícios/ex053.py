print('\033[35m{:-^40}\033[m'.format(' Verificador de Palíndromo !!'))
f = str(input('Digite uma frase: ')).upper().split()
f = ''.join(f)
inverso = f[::-1]
counter = 0

print(inverso)
print('O inverso da {} é {}'.format(f, inverso))
#print('O inverso da {} é '.format(f), end='')

'''for c in range(0, len(f)):
    print((f[len(f) - c - 1]), end='')
    if f[c] != f[(len(f) - c - 1)]:
        counter = counter + 1
'''
#para fazer o teste sem o for eu mudei o condicional do IF
if f != inverso:
    print('\nA frase \033[1:31mNÃO\033[m é um palíndromo!')
else:
    print('\nA frase \033[32:1mÉ\033[m um palíndromo!')
