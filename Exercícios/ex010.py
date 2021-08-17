d = float(input('Quantos reais você tem na sua carteira? '))
cores = {'Vermelho':'\033[31m', 'Limpa':'\033[m'}
print('Com esse valor você pode comprar {}{:.2f}{} doláres!!!'.format(cores['Vermelho'], d/3.27, cores['Limpa']))

