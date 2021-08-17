contador = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
            'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    while True:
        n = int(input('Digite um númeto entre 0 e 20: '))
        if n < 0 or n > 20:
            print('Valor inválido. Tente novamente')
        else:
            break
    print(f'Você escolheu o número {contador[n]}')
    e = str(input('Você quer escolher mais ou número? [S/N] ')).upper().strip()[0]
    if e in "N":
        break
    elif e not in "S":
        print('Inválido! ', end='')
