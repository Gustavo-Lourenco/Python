from math import sqrt, pow, hypot

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
#hip = sqrt(pow(co, 2) + pow(ca, 2))
print('O valor da hipotenusa é: {:.1f}'.format(hypot(co, ca)))




