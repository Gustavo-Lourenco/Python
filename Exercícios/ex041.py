idade = int(input('Digite o seu ano de nascimento para definirmos sua categoria: '))

if idade <= 9:
    print('Sua catergoria é a Mirim')
elif idade > 9 and idade <=14:
    print('Sua categoria é Junior')
elif idade > 14 and idade <=19:
    print('Sua categoria é junior')
elif idade > 19 and idade <= 40:
    print('Sua categoria é senior')
else:
    print('Sua categoria é master')
