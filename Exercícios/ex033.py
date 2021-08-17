n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digete o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1>n2 and n1>n3:
    print('O maior número é o {}'.format(n1))
if n1<n2 and n2<n3:
    print('o menor número é o {}'.format(n1))
if n2>n1 and n2>n3:
    print('O maior número é o {}'.format(n2))
if n2<n1 and n2<n3:
    print('O menor número é o {}'.format(n2))
if n3>n1 and n3>n2:
    print('O maior número é o {}'.format(n3))
if n3<n1 and n3<n2:
    print('O menor número é o {}'.format(n3))