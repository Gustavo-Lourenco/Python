print('\033[31:1m{:-^100}\033[m'.format('Contador de pessoas com mais de 21 anos'))
counter = 0

for c in range(1,8):
    ano = int(input('Qual a idade da {}º pessoa? '.format(c)))
    if ano >= 21:
        counter = counter + 1
print('*' * 100)
if counter <= 0:
    print('\033[1:31mNão pessoas maiores de idade!\033[m')
elif counter == 1:
    print('Há uma pessoa maior de idade!')
else:
    print('Há {} pessoas maiores de idade!'.format(counter))
