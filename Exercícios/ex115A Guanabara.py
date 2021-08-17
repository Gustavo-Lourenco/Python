from ex115.lib.interface import*
from time import sleep

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'Sair'])
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Opção 3. Encerrando o programa ... ')
        break
    else:
        print('\033[31mOpção inválida!\033[m Digite números entre 1 e 3.')
    sleep(1)

