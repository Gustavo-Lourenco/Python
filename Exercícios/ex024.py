cidade = input('Qual o nome da cidade onde você mora? ')
cidade = cidade.lstrip()
cidade = cidade.upper()
cidade = cidade.find('SANTO')

if cidade < 0:
    print('A cidade onde você mora não começa com o nome Santo')
else:
    print('A cidade onde você mora começa com a palavra Santo')

