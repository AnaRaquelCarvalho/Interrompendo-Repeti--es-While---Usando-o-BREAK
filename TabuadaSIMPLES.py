print('-'*46)
while True:
    n = int(input('Quer ver a Tabuada de qual valor ? '))
    print('-'*46)
    if n <= 0:
        break
    for c in range(1,11):
       print(f'{n} x {c} = {n*c}')
    print('-'*46)
print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')
print('-'*46)