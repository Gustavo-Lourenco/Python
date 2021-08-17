teste = 's'
texto = ''
soma = 0
cont = 0
media = 0
maior = 0
menor = 0


while teste == 's':
    if cont == 0:
        n = int(input('Digite um número: '))
        maior = n
        menor = n
        soma = soma + n
        cont += 1
        media = soma / cont
        teste = input('Você quer digitar mais um número? [S/N] ').lower()
    else:
        n = int(input('Digite um número: '))
        soma = soma + n
        cont += 1
        media = soma / cont
        teste = input('Você quer digitar mais um número? [S/N] ').lower()
        if n >= maior:
            maior = n
        if n <= menor:
            menor = n

print('A soma total dos valores é {} e a média é {}'.format(soma, media))
print('O maior número é {} e o menor é {}'.format(maior, menor))