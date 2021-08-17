def nota(*num, sit=False):
    """
    O programa retorna a média, a maior, a menor e a situação (opcional) das notas digitadas
    :param num: Colocar todas as notas que comporão a média
    :param sit: (opcional) Retornar a situação ou não
    :return: Média, Maior, Menor e situação.
    Made By Gustavo Lourenço
    """
    counter = 0
    maior = 0
    menor = 0
    soma = 0
    for c in lista:
        counter += 1
        soma += c
        if counter == 1:
            maior = c
            menor = c
        else:
            if c > maior:
                maior = c
            if c < menor:
                menor =c
    média = soma / counter
    print(f'A quantidade total de notas foi {counter}, a maior nota foi {maior}, '
          f'a menor nota foi {menor} e a média é {média}')
    if sit is True:
        if média < 5:
            print(f'A situação é ruim!')
        if 5 <= média < 7:
            print(f'Situação: Você é medíocre')
        if média > 7:
            print(f'A situação é boa!')


lista = (5, 8, 5, 9, 7)

nota(lista, sit=True)