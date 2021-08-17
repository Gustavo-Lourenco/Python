from random import randint

resultado = teste = cont = 0

print('-' * 100)
print('{:^100}'.format('Jogo do par ou ímpar!'))
print('-' * 100)

while True:
    pc = randint(1, 10)
    while True: #Verificar se o usuário escolheu entre número par ou ímpar.
        escolha = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
        if escolha in 'PI':
            break
        else:
            print('Opção inválida, tente novamente: ')
    n = int(input('Escolha um número: '))
    resultado = pc + n
    teste = resultado % 2
    if escolha == 'P' and teste == 0:
        print(f'O computador escolheu {pc} e você {n}. Você ganhou!!')
        cont += 1
    elif escolha == 'P' and teste == 1:
        print(f'O computador escolheu {pc} e você {n}, portanto você perdeu!')
        break
    elif escolha == 'I' and teste == 0:
        print(f'O computador escolheu {pc} e você {n}, portanto você perdeu!')
        break
    elif escolha == 'I' and teste == 1:
        print(f'O computador escolheu {pc} e você {n}. Você ganhou!!')
        cont += 1
print(f'Você venceu {cont} vezes antes de perder')