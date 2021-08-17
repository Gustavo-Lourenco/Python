km = float(input('Qual a distância percorrida em km? '))
d = float(input('O carro foi alugado por quantos dias? '))
precokm = km*0.15
pdias = 60*d
valor = pdias + precokm
print('Considerando que você alugou o carro por {:.0f} dias e andou {}km\nO valor a ser pago é de R${:.2f}'.format(d, km, valor))
