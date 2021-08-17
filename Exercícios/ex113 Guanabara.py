def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31:1mErro. Por favor digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31:1mO usuário encerrou o programa.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            r = float(input(msg))
        except (TypeError, ValueError):
            print('\033[31:1mErro. Por favor digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31:1mO usuário encerrou o programa.\033[m')
            return 0
        else:
            return r


n1 = leiaInt('Digite o valor inteiro: ')
r1 = leiaFloat('Digite o valor real: ')
print(f'O número inteiro digitado foi {n1} e o real foi {r1}')
