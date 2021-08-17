cadastro = dict()
lista = list()
mulheres = list()
idade_acimamédia = list()
count = 0
média_idade = 0

while True:
    cadastro['nome'] = str(input('Digite o nome da pessoa: '))
    count += 1
    while True:
        cadastro['sexo'] = str(input('Digite o sexo da pessoa: [F/M] ')).upper().strip()
        if cadastro['sexo'] not in 'FM':
            print('Escolha inválida. Digite F ou M. ')
        elif cadastro['sexo'] == 'F':
            mulheres.append(cadastro['nome'][:])
            break
        else:
            break
    cadastro['idade'] = int(input('Qual é a idade da pessoa?  '))
    média_idade += cadastro['idade']
    while True:
        cond = str(input('Quer adicionar mais pessoas? [S/N] ')).upper().strip()
        if cond not in 'SN':
            print('Escolha inváida. Digite S ou N. ')
        else:
            break
    if cond == 'N':
        lista.append(cadastro.copy())
        break
    elif cond == 'S':
        lista.append(cadastro.copy())
média_idade = média_idade/count

for c in range(0, len(lista)):
    if lista[c]['idade'] > média_idade:
        idade_acimamédia.append(lista[c])

print(f'Ao todo foram adicionadas {count} pessoas na lista') #Poderia usar o len de galera
print(f'As mulheres da lista são: ', end='')
for c in mulheres:
    print(f'[{c}]', end=' ')
print(f'\nA média de idade das pessoas é: {média_idade:.1f} anos')
print(f'As pessoas com a idade acima da média são: ')
for c in idade_acimamédia:
    print(f'  => {c}')
