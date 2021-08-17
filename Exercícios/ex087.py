matriz = list()
matriz_2_coluna = list()
pares = 0
soma_3_coluna = 0

for d in range(0,3):
    for c in range(0, 3):
        n = int(input(f'Digite o número da posição [{d} , {c}] : '))
        matriz.append(n)
        if n % 2 == 0:
            pares += n
        if c == 2:
            soma_3_coluna += n
        if d == 1:
            matriz_2_coluna.append(n)

print('-=' * 40)
print(f'[{matriz[0]:^5}]   [{matriz[1]:^5}]   [{matriz[2]:^5}]')
print(f'[{matriz[3]:^5}]   [{matriz[4]:^5}]   [{matriz[5]:^5}]')
print(f'[{matriz[6]:^5}]   [{matriz[7]:^5}]   [{matriz[8]:^5}]')
print('-=' * 40)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {soma_3_coluna}')
print(f'O maior valor da segunda coluna é {max(matriz_2_coluna)}')