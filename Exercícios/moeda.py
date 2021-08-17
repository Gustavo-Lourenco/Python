def aumentar(x):
    y = x*1.1
    print(f'Aumentando 10% temos {y:.2f}')


def dobro(x):
    y = x*2
    print(f'O dobro do valor é R$ {y:.2f}')


def metade(x):
    y = x/2
    print(f'A metade desse valor é R$ {y:.2f}')


def moeda(dinheiro=0, moeda='R$'):
    print(f'{moeda} {dinheiro:>8.2f}'.replace('.', ','))

