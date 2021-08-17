p = float(input('Qual o seu peso? (kg) '))
h = float(input('Qual a sua altura? (m) '))
imc = p/h**2

if imc < 18.5:
    print('Você está abaixo do peso. Cuidado!')
elif 18.5 <= imc < 25:
    print('Você está com o peso ideal.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso!')
elif 30 <= imc < 40:
    print('Você está obeso. Cuidado!!')
else:
    print('Você está com obesidade morbida. \033[1:31mVocê precisa de ajuda!!')
