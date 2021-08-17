def nota(*num, sit=False):
    r = dict()
    r['Quantidade'] = len(num)
    r['Maior'] = max(num)
    r['Menor'] = min(num)
    r['Média'] = sum(num)/len(num)
    return r


lista = nota(2, 3, 4, 7, 9, 10)
print(lista)
