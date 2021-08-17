cont = 0
e = 0
resposta = 0

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))

while cont == 0:
    e = int(input('''Operações possíveis : 
[1] Somar
[2] Multiplicar
[3] Maior
[4] Digitar novos números
[5] Sair do programa
Qual você deseja? '''))
    if e == 1:
        resposta = n1 + n2
        print('\033[1:33m-\033[m' * 100)
        print('A soma dos valores de {} e {} é {}.'.format(n1, n2, resposta))
        print('\033[1:33m-\033[m' * 100)
    elif e == 2:
        resposta = n1*n2
        print('\033[1:33m-\033[m' * 100)
        print('A multiplicação dos valores {} e {} é {}.'.format(n1, n2, resposta))
        print('\033[1:33m-\033[m' * 100)
    elif e == 3:
        if n1 >= n2:
            resposta = n1
            print('\033[1:33m-\033[m' * 100)
            print('Entre {} e {} o maior valor é {}.'.format(n1, n2, resposta))
            print('\033[1:33m-\033[m' * 100)
        else:
            resposta = n2
            print('\033[1:33m-\033[m' * 100)
            print('Entre {} e {} o maior valor é {}.'.format(n1, n2, resposta))
            print('\033[1:33m-\033[m' * 100)
    elif e == 4:
        print('\033[1:33m-\033[m' * 100)
        print('\033[1:36mDigite novos números:\033[m')
        print('\033[1:33m-\033[m' * 100)
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite mais um número: '))
    elif e == 5:
        print('\033[1:33m-\033[m' * 100)
        print('Programa Encerrado')
        print('\033[1:33m-\033[m' * 100)
        cont += 1
    else:
        print('Opção inválida! Tente novamente: ')

