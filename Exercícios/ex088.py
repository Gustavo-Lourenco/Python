from random import sample
from time import sleep

print('-' * 50)
print('{:^50}'.format('Jogo da Mega Sena da Virada'))
print('-' * 50)

n = int(input('Quantos jogos você deseja fazer? '))

print(f'Sorteando {n} jogos')

for c in range(1, n+1):
    print(f'Jogo {c}: ', end=' ')
    print(sample(range(1, 61), 6))
    sleep(0.5)

print('-' * 50)
print('{:^50}'.format('BOA SORTE!!'))
print('-' * 50)
