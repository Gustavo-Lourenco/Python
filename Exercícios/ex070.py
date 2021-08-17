gasto = contp = contp2 = mínimo = cont = 0
nome_show = ''

while True:
    n = str(input('Qual é o nome do produto? '))
    p = float(input('Qual o preço? '))
    gasto += p
    if p > 1000:
        contp += 1
    if cont == 0:
        mínimo = p
        cont += 1
    if mínimo > p:
        mínimo = p
        nome_show = n
    while True:
        teste = str(input('Você quer incluir mais produtos? [S/N] ')).strip().upper()[0]
        if teste in 'SN':
            break
        else:
            print('Opção inválida! Tente novamente: ')
    if teste == 'N':
        break

print(f'O preço total dos produtos é R${gasto:.2f}.')
print(f'{contp} produto(s) custa(m) mais do que R$1000')
print(f'O produto mais barato é o {nome_show} e custou R${mínimo:.2f}')