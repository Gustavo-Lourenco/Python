from random import randint
'''
maior = 0
menor = 0

for c in range(1, 6):
    n = randint(1, 10)
    if c == 2:
        p2 = n
    if c == 3:
        p3 = n
    if c == 4:
        p4 = n
    if c == 5:
        p5 = n

    if c == 1:
        maior = n
        menor = n
        p1 = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n

teste = (p1, p2, p2, p4, p5)
print(f'Os números sorteados foram {teste[0]} {teste[1]} {teste[2]} {teste[3]} {teste[4]}')
print(f'O maior número foi {maior}')
print(f'O menor número foi {menor}')
'''
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os números sorteados foram: ', end='')
for c in range(0, 5):
    print(tupla[c], end=' ')
print(f'\nO maior número sorteado foi {max(tupla)}')
print(f'O menor número sorteado foi {min(tupla)}')
