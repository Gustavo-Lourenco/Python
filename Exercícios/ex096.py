def área(a, b):
    area = a*b
    print(f'A área de um terreno de {a}X{l} é de {area:.1f}m²')


print('-' * 50)
print('Medidor de Terrenos')
print('-' * 50)

a = float(input('Digite o comrimento do terreno: '))
l = float(input('Digite a largura do terreno: '))
área(a, l)

