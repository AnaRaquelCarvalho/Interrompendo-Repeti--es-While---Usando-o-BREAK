print('='*23, 'TABUADA' ,'='*23)
from time import sleep
sleep(3)
print('       SEJA BEM VINDO AO PROGRAMA TABUADA    ')
from time import sleep
sleep(3)
print('='*56)
while True:
    n = int(input('Informe de Qual Tabuada quer ver o valor ? '))
    print('='*46)
    print('''Escolha a tabuada que deseja ver:'
    [1] ADIÇÃO
    [2] SUBTRAÇÃO
    [3] MULTIPLICAÇÃO
    [4] DIVISÃO
    [5] SAIR DO PROGRAMA''')
    opcao = int(input('Opção: '))
    print('='*46)
    if opcao == 1:
        print(f'Tabuada de {n} >>> ADIÇÃO.')
        for c in range(1, 11):
            print(f'{n} + {c} = {n + c}')
    elif opcao == 2:
        print(f'Tabuada de {n} >>> SUBTRAÇÃO.')
        for c in range(1, 11):
            print(f'{c} - {n} = {c - n}')
    elif opcao == 3:
        print(f'Tabuada de {n} >> MULTIPLICAÇÃO ')
        for c in range(1, 11):
            print(f'{n} * {c} = {n * c}')
    elif opcao == 4:
        print(f'Tabuada de {n} >> DIVISÃO ')
        for c in range(1, 11):
            print(f'{n} : {c} = {n / c}')
    elif opcao == 5:
        print(f'Fechando o Programa...')
        from time import sleep
        sleep(3)
        print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')
    else:
        opcao = 0
        break
print('\033[1:31m[{}]'.format(opcao),'OPÇÃO INVÁLIDA - TENTE NOVAMENTE!')
print('='*46)


