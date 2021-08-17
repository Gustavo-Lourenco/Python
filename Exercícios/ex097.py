def escreva (*texto):
    print(f'{"---"}{"-" * (len(t))}{"---"}')
    print(f'{"   "}{t}{"   "}')
    print(f'{"---"}{"-" * (len(t))}{"---"}')


t = str(input('Digite um texto: '))
escreva(t)