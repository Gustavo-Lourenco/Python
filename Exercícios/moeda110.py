def moeda(x=0, y=0, z=0) -> object:
    aumento = x * (z/100 + 1)
    desconto = x * (y/100 + 1)
    print('-' * 30)
    print(f'{"Resumo do Valor":^30}')
    print('-' * 30)
    print(f'{"Preço analisado"} \tR${x:.2f}'.replace('.', ','))
    print(f'{"Dobro do preço"} \t\tR${x * 2:.2f}'.replace('.', ','))
    print(f'{"Metade do Preço"} \tR${x / 2:.2f}'.replace('.', ','))
    print(f'{z}% {"de aumento"} \t\tR${aumento:.2f}'.replace('.', ','))
    print(f'{y}% {"de desconto"} \t\tR${desconto:.2f}'.replace('.', ','))
    print('-' * 30)

