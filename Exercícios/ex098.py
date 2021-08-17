from time import sleep
a1 = b1 = c1 = 0

def contagem(a, b, c):
    print('-=' * 20)
    print('Contagem de {} a {} de {:.0f} em {:.0f}'.format(a, b, (c*c)**0.5, (c*c)**0.5))
    if c == 0:
        c = 1
    if a < b:
        for d in range(a, b+1, c):
            print(d, end=' ')
            sleep(0.2)
        print('FIM')
    else:
        if c > 0:
            c = c * (-1)
        for e in range(a, b-1, c):
            print(e, end=' ')
            sleep(0.2)
        print('FIM')

contagem(0, 10, 1)
contagem(10, 0, -2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
a1 = int(input('Início: '))
b1 = int(input('FIM: '))
c1 = int(input('Passo: '))
contagem(a1, b1, c1)
