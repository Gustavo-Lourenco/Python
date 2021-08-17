t = input('Digite algo ')
#print('\033[31mO tipo primitivo é {}'.format(tyteste(t)))
print('\033[32mSó tem espaços? {} '.format(t.isspace()))
print('\033[33mÉ um número? {}'.format(t.isnumeric()))
print('\033[34mÉ alfabético? {}'.format(t.isalpha()))
print('\033[36mÉ maiúsculo? {}'.format(t.isupper()))
print('\033[37mÉ minúsculo? {}'.format(t.islower()))
print('\033[7mÉ capitalizado? {}'.format(t.istitle()))

