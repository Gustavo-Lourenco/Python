from datetime import date

ano = int(input('Digite o ano do seu nascimento: '))
x = date.today().year - ano

if x == 18:
    print('Você deve se alistar ainda esse ano!!')
elif x < 18:
    print('Você deve se alistar em {} anos'.format(18-x))
else:
    print('Você deveria ter se alistado há {} anos atrás'.format(x-18))
    print('\033[1:31mShame on you!!!')
