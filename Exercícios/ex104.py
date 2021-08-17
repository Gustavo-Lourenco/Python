def leiaInt(num):
    if n.isnumeric():
        print(f'O número escolhido foi {n}')
    else:
        print(f'\033[31:1mO valor escolhido não é um número\033[m')


n = str(input('Digite um número: '))
leiaInt(n)