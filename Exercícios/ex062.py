cont = 0
termos = 10
teste = 'sim'
first = 0
teste2 = 0

n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

print('-' * 100)
print('{:^100}'.format('A progressão aritmética é ... '))
print('-' * 100)

while teste == 'sim':
    teste2 = 0
    while cont < termos:
        if cont == 0 and first == 0:
            print(n1, end=' ')
            cont += 1
        else:
            n1 += r
            print(n1, end=' ')
            cont += 1
    while teste2 == 0:
        teste = str(input('\nVocê quer adicionar mais elementos na PA? [Sim / Não] '))
        if teste == 'sim':
            termos = int(input('Quantos termos você deseja adicionar? '))
            cont = 0
            first = 1
            teste2 = 1
        elif teste == 'não':
            teste = 'não'
            teste2 = 1
        else:
            print('\033[1:31mOpção inválida! Escolha entre Sim e Não.\033[m')
            teste2 = 0
