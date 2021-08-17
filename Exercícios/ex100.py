from random import randint
from time import sleep

num = list()


def aleatório(list):
    print('Sorteando os valores da lista:', end=' ')
    for c in range(0, 5):
        num.append(randint(0, 9))
    for d in num:
        sleep(0.3)
        print(d, end=' ')

def somapar(list):
    count = 0
    print('\nSomando os valores pares de :', end =' ')
    for c in num:
        print(c, end=' ')
        if c % 2 == 0:
            count += c
    print(f'Temos {count}')


aleatório(num)
somapar(num)
