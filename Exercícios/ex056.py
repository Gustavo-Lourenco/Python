media = 0
maior_idade = 0
nome_velho = 0
counter = 0

print('\033[1:31m{:*^100}\033[m'.format(' Desafio 56 - Teste Final da Estrutura For '))

for c in range(1, 5):
    nome = input('Qual o nome da {}º pessoa? '.format(c))
    idade = int(input('Qual a idade da {}º pessoa? '.format(c)))
    sexo = input('Qual o gênero da {}º pessoa? '.format(c)).capitalize()
    media = media + idade 
    if c == 1:     #Condiação para achar o homem mais velho
        maior_idade = idade
        nome_velho = nome
    else:
        if maior_idade <= idade and sexo == 'Masculino':
            maior_idade = idade
            nome_velho = nome
    if sexo == 'Feminino' and idade < 20:  #Condição para as mulheres com menos de 20 anos
        counter = counter + 1

print('*' * 100)
print('A média de idade do grupo é {:.1f} anos. '.format(media/c))
print('O homem mais velho é o {} e ele tem {} anos.'.format(nome_velho, maior_idade))
print('Há {} mulher(es) com menos de 20 anos.'.format(counter))