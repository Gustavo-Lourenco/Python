'''num = (input('Digite um número entre 0 e 9999: '))
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))'''

num = int(input('Digite um número qualquer: '))
milhar = num//1000 % 10
centena = num//100 % 10
dezena = num//10 % 10
unidade = num//1 % 10
print('O número digitado foi ', num,)
print('O milhar do número é: {}'.format(milhar))
print('A centena do número digitado é: {}'.format(centena))
print('A dezena do número digitado é: {}'.format(dezena))
print('A unidade do número digitado é: {}'.format(unidade))