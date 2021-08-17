import moeda110


def leiadinheiro():
    valido = False
    while not valido:
        entrada = str(input('Digite o valor: ')).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('Valor inválido!! Digite novamente: ')
        else:
            return float(entrada)


leiadinheiro()