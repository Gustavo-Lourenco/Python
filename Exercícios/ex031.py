km = float(input('Qual a distância da viagem (km)?: '))

if km<=200:
    valor=km*0.5
    print('O valor total da sua viagem é de R${:.2f}'.format(valor))
else:
    valor=km*0.45
    print('O valor da sua viagem é de R${:.2f}'.format(valor))

print('Boa viagem!!!')
