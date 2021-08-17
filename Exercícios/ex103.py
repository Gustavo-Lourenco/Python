def ficha(a='Desconhecido', b=0):

    print(f'O jogador {a} fez {b} gols no campeonato!')


nome = str(input('Digite o nome do jogador: '))
gol = (input('Quantos gols o jogador fez? '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    nome = 'Desconhecido'
ficha(nome, gol)