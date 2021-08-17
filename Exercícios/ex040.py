from statistics import mean

n1 = float(input('Digite o valor da sua primeira nota: '))
n2 = float(input('Digite o valor da sua segunda nota: '))

media = mean([n1, n2])

if media < 5:
    print('\033[1:31mVocê foi reprovado! Viva com a vergonha!!!')
elif media >= 5 and media < 7:
    print('Você é M de mediocre. A sua nota foi {}'.format(media))
else:
    print('Parábens!!! Você é digno!!!')
