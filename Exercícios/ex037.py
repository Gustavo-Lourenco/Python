n = int(input('Digite um número: '))
print('Você quer converter esse número para binário, octal ou hexadecimal? ')
print('Digite:\n1 - Para binário\n2 - Para octal\n3 - Para hexadecimal ')
x = int(input('Qual a sua escolha? '))

if x == 1:
    print('{} em binário corresponde a {}'.format(n, bin(n)[2:]))
elif x == 2:
    print('{} em octal corresponde a {}'.format(n, oct(n)[2:]))
elif x == 3:
    print('{} em hexadecimal corresponde a {}'.format(n, hex(n)[2:]))
else:
    print('\033[1:31mEscolha inválida!!')

