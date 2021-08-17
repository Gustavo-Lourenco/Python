from time import sleep

def maior(*num):
    """
    :param num: Coloque uma lista com números inteiros
    :return: Retorna o maior número da lista.
    Made by: Gustavo Lourenço
    """
    greater = cont =0
    print('-' * 40)
    print(f'Analisando os valores:', end=' ')
    for c in num:
        if cont == 0:
            greater = c
            cont += 1
            print(c, end=' ')
        else:
            cont += 1
            sleep(0.3)
            print(c, end=' ')
            if c > greater:
                greater = c
    print(f'\nO maior número é: {greater}')


maior(2, 3, 4, 9, 6, 15, 1)
maior(3, 6, 8, 9)
maior(-3, -6, -8, -9)

help(maior)