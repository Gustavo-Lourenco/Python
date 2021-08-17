matriz = list()

for c in range(0, 3):
    n = int(input(f'Digite o número da posição [0 , {c}] : '))
    matriz.append(n)
for d in range(0, 3):
    n = int(input(f'Digite o número da posição [1 , {d}] : '))
    matriz.append(n)
for e in range(0, 3):
    n = int(input(f'Digite o número da posição [2 , {e}] : '))
    matriz.append(n)

print(f'[{matriz[0]:^5}]   [{matriz[1]:^5}]   [{matriz[2]:^5}]')
print(f'[{matriz[3]:^5}]   [{matriz[4]:^5}]   [{matriz[5]:^5}]')
print(f'[{matriz[6]:^5}]   [{matriz[7]:^5}]   [{matriz[8]:^5}]')
