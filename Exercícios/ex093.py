hist = dict()
gols = list()
total = 0

hist['Nome'] = str(input('Digite o nome de um jogador: '))

partidas = int(input('Quantas partidas esse jogador jogou ? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols o {hist["Nome"]} fez no {c+1}º jogo? ')))
    total += gols[c]
hist['Gols'] = gols
hist['Total'] = total

print('-=' * 25)
print(hist)
print('-=' * 25)
for c, v in hist.items():
    print(f'O campo {c} tem o valor {v}')
print('-=' * 25)
print(f'O jogador {hist["Nome"]} jogou {partidas} partidas. ')
for c, v in enumerate(gols):
    print(f'   - Na {c+1}º partida ele fez {v} gols')
print(f'No total o {hist["Nome"]} fez {hist["Total"]} gols')
