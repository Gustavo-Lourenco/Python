nome = input('Qual é o seu nome completo? ')
nome = nome.strip()
count = nome.count(' ')
print('O seu primeiro nome é {} e o último é {}'.format(nome.split()[0], format(nome.split()[count])))

