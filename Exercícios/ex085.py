par = list()
ímpar = list()
geral = list()

for c in range(1, 8):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        par.append(n)
    else:
        ímpar.append(n)

geral.append(par[:])
geral.append(ímpar[:])

print(f'Os valores pares são {sorted(geral[0])} e os ímpares são {sorted(geral[1])}')
