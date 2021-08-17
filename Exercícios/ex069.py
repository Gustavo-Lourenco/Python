cont = 1
contp = conth = contm = 0

while True:
    idade = int(input(f'Digite a idade da {cont}º pessoa: '))
    while True:  # Verifica se o usuário digitou corretamente
        sexo = str(input(f'Digite o sexo da {cont}º pessoa: [F/M] ')).strip().upper()[0]
        if sexo in 'FM':
            break
        else:
            print('Opção inválida, tente novamente!')
    if idade > 18:  # Contador dos maiores de idade
        contp += 1
    if sexo == 'M':  # Contador dos homens
        conth += 1
    if sexo == 'F' and idade < 20:  # Contador das mulheres com menos de 20 anos
        contm += 1
    while True:  # Verifica se o usuário digitou corretamente
        teste = str(input('Você quer adicionar mais alguma pessoa? [S/N] ')).strip().upper()[0]
        if teste in 'SN':
            break
        else:
            print('Opção inválida, tente novamente!')
    cont += 1  # Contador do looping
    if teste == 'N':
        break
print(f'No total {contp} pessoas têm mais do que 18 anos.')
print(f'{conth} Homens foram adicionados a lista.')
print(f'Há no total {contm} mulheres com menos de 20 anos.')
print('PROGRAMA ENCERRADO')
