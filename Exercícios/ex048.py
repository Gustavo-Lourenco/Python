soma = 0

for c in range(1, 500+1):
    if c%2 == 1 and c%3 == 0:
        soma = soma + c
print('A soma dos números ímpares divisiveis por 3 é : {}'.format(soma))
