v = float(input('Qual a velocidade do veículo? '))
if v >80:
    print('Você foi multado por excesso de velocidade!!')
    valor = (v-80)*7
    print('O valor da multa é de R${:.2f}'.format(valor))
else:
    print('You are good to pass')