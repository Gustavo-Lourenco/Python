from datetime import datetime
CLT = dict()

CLT['Nome'] = str(input('Qual o nome da pessoa? '))
ano = int(input('Qual o ano de nascimento da pessoa? '))
CLT['idade'] = datetime.now().year - ano
CLT['CTPS'] = int(input('Qual o número da carteira de trabalho? '))
if CLT['CTPS'] != 0:
    ano_contratação = int(input('Qual foi o ano de contratação? '))
    CLT['Aposentadria'] = 35 + (ano_contratação - ano)
    CLT['Salário'] = int(input('Qual foi o salário inicial? '))

for c, v in CLT.items():
    print(f'{c} - {v}')
