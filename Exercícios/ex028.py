import random
from time import sleep

n = int(input('Digite um número entre 0 e 5: '))
r = random.randint(0,5)

print('Processando ...')
sleep(3)

if n == r:
    print('Parábens você acertou!!!')
else:
    print('Você perdeu, tente novamente!')
