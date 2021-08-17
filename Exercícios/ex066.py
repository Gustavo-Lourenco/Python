soma = cont = 0

while True:
    n = int(input('Digite um valor: [999 Para parar] '))
    if n == 999:
        break
    soma += n
    cont += 1

print(f'Foram digitados {cont} números e a soma dele é {soma}')