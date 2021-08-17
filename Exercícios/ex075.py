m1 = m2 = m3 = m4 = ''

for c in range(1, 5):
    n = int(input('Digite um valor no teclado:  '))
    if c == 1:
        n1 = n
        if n % 2 == 0:
            m1 = n
    if c == 2:
        n2 = n
        if n % 2 == 0:
            m2 = n
    if c == 3:
        n3 = n
        if n % 2 == 0:
            m3 = n
    if c == 4:
        n4 = n
        if n % 2 == 0:
            m4 = n

vetor = (n1, n2, n3, n4)
vetor2 = (m1, m2, m3, m4)
print(f'Os números digitados foram: {vetor}')
print(f'O número 9 apareceu {vetor.count(9)} vez(es)')
if vetor.count(3) != 0:
    print(f'O número 3 aparece primeiro na posição {vetor.index(3) + 1}')
else:
    print('O número 3 nao foi digitado')
print(f'Os números pares digitados foram {vetor2[0]} {vetor2[1]} {vetor2[2]} {vetor2[3]}')
