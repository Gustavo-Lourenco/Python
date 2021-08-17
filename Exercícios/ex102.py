def fatorial(num, show=False):
    """
    :param num: Digite o número que você quer que seja fatorado
    :param show: (Opcional) Se estiver em show, mostrará o cálculo feito
    :return: O número fatorado
    Made by Gustavo Lourenço
    """
    valor = 1
    if num == 0:
        print(1)
    else:
        if show is False:
            for c in range(num, 1, -1):
                valor *= c
            print(valor)
        else:
            for c in range(num, 0, -1):
                if c == 1:
                    print(f'{c} = {valor}', end='')
                else:
                    print(f'{c} X', end=' ')
                    valor *= c


num = int(input('Digite o número a ser fatorado: '))
fatorial(num, show=False)
