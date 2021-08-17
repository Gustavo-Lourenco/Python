n = 0
m = ''

sexo = str(input('Digite o sexo da pessoa: [M/F] ')).upper().strip()[0]

while sexo not in 'MF':
    sexo = str(input('Dados inválidos!! Digite o valor correto!!')).upper().strip()[0]

'''while n == 0:
    m = str(input('Digite o sexo da pessoa [F/M] : ')).strip().upper()[0]
    if m in 'FM':
        n += 1
    else:
        print('Opção inválida : ')'''
print('Fim do teste')