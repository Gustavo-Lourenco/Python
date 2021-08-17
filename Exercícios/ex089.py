mean = list()
n1_list = list()
n2_list = list()
n_list = list()
geral = list()
nome = list()
cont = i = 0

while True:
    aluno = str(input('Digite o nome do(a) aluno(a): '))
    nome.append(aluno)
    n1 = float(input('Digite a 1º nota: '))
    n1_list.append(n1)
    n2 = float(input('Digite a 2º nota: '))
    n2_list.append(n2)
    média = (n1+n2) / 2
    mean.append(média)
    cont += 1
    #geral.append([nome], [n1, n2], [media]) - Esse comando substitui todas as adições na listas individualmente
    while True: #Verificar se o usuário escolheu entre sim e não
        continuar = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
        if continuar not in 'SN':
            print('Escolha inválida. ', end='')
        else:
            break
    if continuar in 'N': #Verifica se o usuário quis sair do programa
        break

n_list.append(n1_list)
n_list.append(n2_list)
geral.append(nome)
geral.append(n_list)
geral.append(mean)

print('-=' * 25)
print('{:<10}{:<30}{:<30}'. format('Número', 'Nome', 'Média'))
print('-' * 50)
for c in range(0, cont):
    print(f'{c+1:<10}{geral[0][c]:<30}{geral[2][c]:<30}')
print('-' * 50)

while True:
    i = int(input('Mostrar nota de qual aluno? [999 para sair] '))
    if i == 999:
        break
    elif i-1 not in range(cont):
        print('Não há aluno {}, tente novamente. '.format(i))
    else:
        print('-' * 50)
        print(f'Notas de {geral[0][i-1]} são {geral[1][0][i-1]} e {geral[1][1][i-1]}')
        print('-' * 50)

print('-' * 50)
print('Programa encerrado!!!\nVolte Sempre!')