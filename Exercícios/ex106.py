from time import sleep


def ajuda(txt):
    print('\033[37m')
    print(help(txt))
    print('\033[m')


while True:
    print('\033[31m-' * 40)
    print('{:^40}'.format('Sistema de ajuda PyHelp'))
    print('-' * 40, '\033[m')
    txt = str(input('Função ou biblioteca: ')).lower().strip()
    if txt == 'fim':
        break
    print('\033[35m-' * 40)
    print('{:^40}'.format('Acessando o manual do Pyhelp'))
    print('-' * 40, '\033[m')
    sleep(2)
    ajuda(txt)

print('Fim do programa')