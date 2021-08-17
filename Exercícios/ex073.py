tabela = ('Bragantino', 'Athletico-PR', 'Palmeiras', 'Fortaleza', 'Bahia', 'Santos', 'Atlético-GO', 'Atlético-MG',
        'Fluminense', 'Flamengo', 'Corinthians', 'Ceará SC', 'Internacional', 'Juventude', 'Sport Recife', 'Cuiabá',
        'São Paulo', 'Chapecoense', 'América-MG', 'Grêmio')
chape = tabela.index('Chapecoense')

print(f'Os 5 primeiros colocados são: {tabela[:5]}')
print(f'Os 4 últimos colocados são: {tabela[16:]}')
print(f'Os times em ordem alfabética são: {sorted(tabela)}')
print(f'A Chapecoense está na posição {chape}')
