aluno = dict()
aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Média'] = float(input(f'Digite a média do {aluno["Nome"]}: '))
if aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado'
elif 5 <= aluno['Média'] <= 7:
    aluno['Situação'] = 'Medíocre mas aprovado'
else:
    aluno['Situação'] = 'Aprovado com louvor'

#print(f'O aluno {aluno["Nome"]} teve média {aluno["Média"]} e a situação é {aluno["Situação"]}')
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
