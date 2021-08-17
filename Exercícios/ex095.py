hist = dict()
tabela = list()
gols = list()
total = 0
count = 1

while True:
    hist['Nome'] = str(input('Digite o nome de um jogador: '))
    partidas = int(input('Quantas partidas esse jogador jogou ? '))
    total = 0 #Zera o total de gols para a contagem do próximo jogador
    gols.clear() #Zera o total de gols para a contagem do próximo jogador
    for c in range(0, partidas):
        gols.append((int(input(f'Quantos gols o {hist["Nome"]} fez no {c+1}º jogo? '))))
        total += gols[c]
    hist['gol'] = gols[:]
    hist['Total'] = total
    tabela.append(hist.copy())
    while True:
        resposta = str(input('Deseja adicionar outro jogar? [S/N] ')).upper()
        if resposta in 'SN':
            break
        print('Valor inválido, digite S ou N. ', end='')
    if resposta == 'N':
        break
print(tabela)

print('-=' * 25)
print('{:<5}{:<15}{:<10}{:<20}'. format('Nº', 'Nome', 'Total', 'Gols'))
print('-' * 50)

for c in range(0, len(tabela)):
        print(f'{c:<5}{tabela[c]["Nome"]:<15}{tabela[c]["Total"]:<10}{tabela[c]["gol"]}')
print('-' * 50)

while True:
    while True:
        escolha = int(input('Mostrar os dados de qual jogador? [999 para sair] '))
        if escolha <= len(tabela)-1 or escolha == 999:
            break
        print('Digito inválido, tente novamente. ')
    if escolha == 999:
        break
    print(f'Levantamento do jogador {tabela[escolha]["Nome"]}')
    for g in tabela[escolha]['gol']:
        print(f'No jogo {count} ele fez {g} gols')
        count += 1
    count = 1
    print('-' * 50)