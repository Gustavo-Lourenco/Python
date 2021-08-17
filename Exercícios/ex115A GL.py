#Programa 115 o Desafio FINAL!
while True:
    try:
        print('-' * 30)
        print(f'{"Menu Principal":^30}')
        print('-' * 30)
        print('\033[33m1 -\033[m \033[36mVer pessoas cadastradas\033[m')
        print('\033[33m2 -\033[m \033[36mCadastrar nova pessoa\033[m')
        print('\033[33m3 -\033[m \033[36mSair do sistema\033[m')
        print('-' * 30)
        opcao = int(input('Qual a sua opção? '))
    except (ValueError, TypeError):
        print('Opção inválida! Tente novamente.')
    else:
        if opcao == 1:
            print('-' * 30)
            print(f'{"Opção 1":^30}')
            print('-' * 30)
        elif opcao == 2:
            print('-' * 30)
            print(f'{"Opção 2":^30}')
            print('-' * 30)
        elif opcao == 3:
            print('-' * 30)
            print(f'{"Opção 3":^30}')
            print(f'{"Encerrando programa ...":^30}')
            print('-' * 30)
            break
        else:
            print('Opção inválida! Digite números entre 1 e 3.')
