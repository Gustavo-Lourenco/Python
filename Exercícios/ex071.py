print('-' * 100)
print('{:^100}'.format('Bem vindo ao PoteBANK'))
print('-' * 100)

c50 = 0

# Cédulas de 50, 20, 10 e 1
while True:
    n = int(input('Qual o valor que você deseja sacar? '))
    c50 = n // 50
    c20 = (n - c50 * 50) // 20
    c10 = (n - c50 * 50 - c20 * 20) // 10
    c1 = (n - c50 * 50 - c20 * 20 - c10 * 10) // 1
    if c50 != 0:
        print(f'Total de {c50} cédulas de R$50,00')
    if c20 != 0:
        print(f'Total de {c20} cédulas de R$20,00')
    if c10 != 0:
        print(f'Total de {c10} cédulas de R$10,00')
    if c1 != 0:
        print(f'Total de {c1} cédulas de R$1,00')
    break
print('-' * 100)
print('{:^100}'.format('Volte sempre ao PoteBANK'))
print('-' * 100)

