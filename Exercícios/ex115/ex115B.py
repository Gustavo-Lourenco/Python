from ex115.lib.interface import*
from ex115.lib.arquivo import*
from time import sleep

arq = 'lista.txt'

if not arqExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'Sair'])
    if resposta == 1: # Opção de Listar Arquivos
        cabeçalho('Opção 1')
        lerArquivo(arq)
    elif resposta == 2: # Opção cadastrar uma nova pessoa
        cabeçalho('Novo cadastro')
        nome = str(input('Digite o nome da pessoa: '))
        idade = leiaInt('Digite a idade da pessoa: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3: # Sair do programa
        cabeçalho('Opção 3. Encerrando o programa ... ')
        break
    else:
        print('\033[31mOpção inválida!\033[m Digite números entre 1 e 3.')
    sleep(1)
    sorted()