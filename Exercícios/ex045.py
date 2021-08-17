import random
import time

print('{:-^40}'.format(' JOKENPÔ '))

while True:
    while True:
        x = str(input('Escolha entre: Pedra, Papel ou Tesoura: ')).capitalize()
        if x in 'PedraPapelTesoura':
            break
        else:
            print('Opção Inválida! Tente novamente. ')

    lista = ('Pedra', 'Papel', 'Tesoura')
    # Computador escolhe o número e o converte em pedra, papel ou tesoura.
    computador = random.randint(0, 2)
    y = lista[computador]

    print('-' * 20, 'Loading', '-' * 20)
    time.sleep(2)

    if x == y:
        print('Vocês dois escolheram {}. É um empate!.'.format(x))
    elif x == 'Pedra' and y == 'Tesoura':
        print('O computador escolheu {} e você escolheu {}.'.format(y, x))
        print('\033[1:33mParabens!! Você Venceu!!')
    elif x == 'Pedra' and y == 'Papel':
        print('O computador escolheu {} e você escolheu {}.'.format(y, x))
        print('\033[1:31mVocê perdeu. Viva com a vergonha!!')
    elif x == 'Papel' and y == 'Tesoura':
        print('O computador escolheu {} e você escolheu {}.'.format(y, x))
        print('\033[1:31mVocê perdeu. Viva com a vergonha!!')
    elif x == 'Papel' and y == 'Pedra':
        print('O computador escolheu {} e você escolheu {}.'.format(y, x))
        print('\033[1:33mParabens!! Você Venceu!!')
    elif x == 'Tesoura' and y == 'Pedra':
        print('O computador escolheu {} e você escolheu {}.'.format(y, x))
        print('\033[1:31mVocê perdeu. Viva com a vergonha!!')
    elif x == 'Tesoura' and y == 'Papel':
        print('O computador escolheu {} e você escolheu {}.'.format(y, x))
        print('\033[1:33mParabens!! Você Venceu!!')

    escolha = str(input('\033[mGostaria de jogar mais uma vez? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break
