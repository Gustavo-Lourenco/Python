def aumentar(x, z=False):
    y = x*1.1
    if z is False:
        print(f'Aumentando 10% temos {y}')
    else:
        print(f'Aumentando 10% temos R$ {y:>8.2f}'.replace('.', ','))

    # return x if z is False else moeda(res) - O Guanabara usou essa forma para solucionar e res é o nosso Y


def dobro(x, z=False):
    y = x*2
    if z is False:
        print(f'O dobro do valor é {y}')
    else:
        print(f'O do valor é R$ {y:>8.2f}')


def metade(x, z=False):
    y = x/2
    if z is False:
        print(f'A metade desse valor é {y}')
    else:
        print(f'A metade desse valor é R$ {y:>8.2f}')


