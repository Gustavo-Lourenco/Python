cont = 0
cont2 = 0
n = 0

print('*' * 100)
print('{:^100}'.format('Somador de números'))
print('{:^100}'.format('Para para o programa digite 999'))
print('*' * 100)

while n != 999:
    n = int(input('Digite um número qualquer: '))
    if n != 999:
        cont += n
        cont2 += 1

print('Foram digitados {} números e a soma deles é {}'.format(cont2, cont))