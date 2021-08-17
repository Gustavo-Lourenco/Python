aux = list()
dados = list()
pmaior = list()
pmenor = list()

continuar = ''
contp = contpeso = contpesomenor = 0

while True:
    aux.append(str(input('Digite o nome da pessoa: ')))
    contp += 1
    aux.append(int(input('Digite o peso da pessoa: ')))
    dados.append(aux[:])
    aux.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

for p in dados:
    if p[1] > 80:
        pmaior.append(p[0])
        contpeso += 1
    elif p[1] < 50:
        pmenor.append(p[0])
        contpesomenor += 1

print(f'Foram cadastradas {contp} pessoas.')
print(f'{contpesomenor} pessoas tem peso abaixo de 50kg. Elas são {pmenor}')
print(f'{contpeso} pessoas tem o peso maior que 80kg. Elas são {pmaior}')
