from random import randint
from time import sleep
from operator import itemgetter
torneio = {'Jogador 1':randint(1, 6),
           'Jogador 2':randint(1, 6),
           'Jogador 3':randint(1, 6),
           'Jogador 4':randint(1, 6)}
ranking = dict()
for c, k in torneio.items():
    print(f'O {c} tirou {k} no dado.')
    sleep(0.5)
ranking = sorted(torneio.items(), key=itemgetter(1), reverse=True) # (1) para colocar em rodem de valor

print('-' * 50)
print('{:^50}'.format('Ranking'))
print('-' * 50)
for c, k in enumerate(ranking):
    print(f'O {c}º {k[0]} tirou {k[1]}')
