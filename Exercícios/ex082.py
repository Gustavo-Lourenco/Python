lista = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    while True:
        s = str(input('Você quer continuar? ')).strip().upper()[0]
        if s in 'SN':
            break
        else:
            print('Tente novamente. ')
    if s == 'N':
        break

par = lista[:]
impar = lista[:]

for c in range(len(par) - 1, 0, -1):
    if par[c] % 2 == 1:
        par.pop(c)

for d in range(len(impar) - 1, 0, -1):
    if impar[d] % 2 == 0:
        impar.pop(d)

print(f'A lista digitada foi {lista}')
print(f'A lista de números pares é: {par}')
print(f'A lista de números ímpares é: {impar}')