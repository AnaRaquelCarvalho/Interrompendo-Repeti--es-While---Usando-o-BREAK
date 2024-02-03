print('='*46)
print(f'         VAMOS JOGAR PAR OU ÍMPAR ?          ')
print('='*46)
v = 0
from random import randint
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e computador {computador}. Total de {total} ',end = ' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!!!')
            v += 1
        else:
            print('Você Perdeu!!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu!!!')
            v += 1
        else:
            print('Você Perdeu!!!')
            break
        print('='*46)
    print('Vamos jogar novamente...')
print('=' * 46)
print(f'GAME Over!!! Você venceu {v} vezes.')
print('='*46)
