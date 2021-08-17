r = i = 0
while True:
    i = str(input('Digite um número inteiro: ')).strip()
    if i.isnumeric() and i not in ".":
        print('Número válido.')
        break
    else:
        print('\033[31:1mErro. Por favor digite um número inteiro válido.\033[m')

while True:
    r = str(input('Digite um número real: '))
    if r.isnumeric():
        print('Número válido')
        break
    else:
        print('\033[31:1mErro. Por favor digite um número inteiro válido.\033[m')

print(f'O número inteiro foi {i} e o real foi {r}')