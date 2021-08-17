from math import pow, sqrt

a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))

mbc = sqrt(pow(b-c, 2))
mac = sqrt(pow(a-c, 2))
mab = sqrt(pow(a-b, 2))

cond1 = 0
cond2 = 0
cond = 0

if mbc < a < (b + c):
    cond1 = 1
if mac < b < (a + c):
    cond2 = 1
if mab < c < (a + b):
    cond3 = 1

if cond1 == 1 and cond2 == 1 and cond3 == 1:
    print('É um triângulo!!')
    if a == b == c:
        print('Equilátero!')
    elif a != b != c != a:
        print('Escaleno!')
    else:
        print('Isóceles!')
else:
    print('NÃO pode ser um triângulo!!')