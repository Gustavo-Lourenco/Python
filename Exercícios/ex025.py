nome = input('Digite o seu nome completo: ').strip()
#print('O seu nome tem Silva: {}'.format('Silva' in nome.title()))
nome = nome.upper()
nome = nome.find('SILVA')

if nome > 0:
    print('Esse nome contém o nome Silva')
else:
    print('Esse nome não contém o nome Silva')
