lista = []

while True:
    n = int(input('Digite um número: '))
    if n in lista:
        print('Valor duplicado, não vou adicionar!')
    else:
        lista.append(n)
    while True:  #Verifica se digitou sim ou não
        continuar = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
        if continuar not in "SN":
        #if continuar != 'S' and continuar != 'N':
            print('Valor inválido, tente novamente.')
        else:
            break
    if continuar == 'N':
        break

print(f'Você digitou os valores: {sorted(lista)}')