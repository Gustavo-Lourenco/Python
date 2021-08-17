def voto(ano):
    """
    :param ano: Entre com o ano do seu nascimento
    :return: A sua idade e se você está apto ou não a votar.
    Made by: Gustavo Lourenço
    """
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade < 16:
        print(f'Com {idade} anos o voto é proibido.')
    if 16 <= idade < 18 or idade >= 65:
        print(f'Com {idade} anos o voto é opcional')
    if 18 <= idade < 65:
        print(f'Com {idade} anos o voto é obrigatório.')


ano = int(input('Qual o seu ano de nascimento? '))
voto(ano)