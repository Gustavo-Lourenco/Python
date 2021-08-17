from random import randint
print('\033[1:31m{:-^140}\033[m'.format(' Jogo para adivinhar em qual número o computador pensou!! '))

computador = randint(0, 10)
jogador = -1
teste = 0
counter = 1

while teste == 0:
    jogador = int(input('Digite o número escolhido: '))
    if jogador == computador:
        print('\033[1:35mParábens você acertou!!!\033[m')
        print('Foram necessárias \033[1:31m{}\033[m tentativas.'.format(counter))
        teste += 1
    else:
        print('\033[31mOpção incorreta. Tente novamente: \033[m')
        counter += 1


