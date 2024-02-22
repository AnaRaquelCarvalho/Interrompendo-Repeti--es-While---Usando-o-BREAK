print('-=-'*16)
from time import sleep
print('{:^46}'.format('BANCO ARC - CARVALHO'))
print('=-='*16)
sleep(2)
saldo = saldo1 = saldo2 = saldo3 = 0
saque = saque1 = saque2 = saque3 = 0
deposito = deposito1 = deposito2 = 0
opcao = opcao1 = opcao2 = opcao4 = 0
print('{:^46}'.format('BEM VINDO! AO AUTOATENDIMENTO'))
print('{:^46}'.format('SELECIONE A OPÇÃO DESEJADA'))
print('=-=' * 16)
while opcao != 4:
    print('''        [1] SALDO
        [2] SAQUE
        [3] DEPÓSITO
        [4] SAIR DO PROGRAMA''')
    print('=-=' * 16)
    opcao = int(input('Qual a sua opção: '))
    print('=-='* 16)
    if opcao == 1:
        print('{:^46}'.format('SALDO DISPONÍVEL PARA SAQUE R$ 3.000'))
        resposta = ' '
        print('=-=' * 16)
        sleep(2)
        while resposta not in 'SN':
            resposta = str(input('DESEJA CONTINUAR [S/N] >>> ')).strip().upper()[0]
        print('=-='* 16)
        sleep(2)
        if resposta == 'N':
            sleep(2)
            print('{:^16}'.format('FINALIZANDO PROGRAMA...'))
            sleep(2)
            break
        if resposta == 'S':
            while opcao1 != 2:
                sleep(2)
                print('{:^46}'.format('SELECIONE UMA DAS OPÇÕES ABAIXO:'))
                print('''               [1] SAQUE
               [2] DEPÓSITO''')
                print('=-=' * 16)
                opcao1 = int(input('INFORME SUA OPÇÃO: '))
                print('=-='* 16)
                sleep(2)
                if opcao1 == 1:
                    saque1 = float(input('INFORME O VALOR DO SAQUE R$ '))
                    saldo1 = 3000 - saque1
                    print(f'Saldo atual Disponivel PARA SAQUE R$ {saldo1:.2f}')
                    print('=-='*16)
                    sleep(3)
                    print('{:^16}'.format('FINALIZANDO PROGRAMA...'))
                    print('=-=' * 16)
                    sleep(3)
                    print('=-=' * 16)
                    print('{:^16}'.format('PROGRAMA FINALIZADO COM SUCESSO!'))
                    print('{:^16}'.format('VOLTE SEMPRE AO BANCO ARC - CARVALHO!'))
                    print('{:^36}'.format('Tenha um Bom Dia!'))
                    print('=-=' * 16)
                    break
                elif opcao1 == 2:
                    deposito1 = float(input('INFORME O VALOR DO DEPÓSITO R$ '))
                    saldo1 = deposito1 + 3000
                    print('=-=' * 16)
                    sleep(2)
                    print(f'Saldo atual Disponivel R$ {saldo1:.2f}')
                    print('=-=' * 16)
                    sleep(3)
                    print('FINALIZANDO O PROGRAMA...')
                    print('=-=' * 16)
                    terminando = ''
                    sleep(3)
                    while terminando not in 'S':
                        if terminando == 'S':
                            print('{:^16}'.format('PROGRAMA FINALIZADO COM SUCESSO!'))
                    print('{:^16}'.format('VOLTE SEMPRE AO BANCO ARC - CARVALHO!'))
                    print('{:^36}'.format('Tenha um Bom Dia!'))
                    print('=-=' * 16)
                    break
    if opcao == 2:
        sleep(2)
        print('{:^16}'.format('{:^16}'.format('SELECIONE A OPÇÃO DESEJADA OU DIGITE O VALOR DO SAQUE')))
        while opcao != 8:
            print('''            [1] R$ 10.00
            [2] R$ 20.00
            [3] R$ 40.00
            [4] R$ 50.00
            [5] R$ 100.00
            [6] R$ 300.00
            [7] R$ 600.00
            [8] R$ 1.000 
            [9] OUTROS VALORES''''')
            print('=-=' * 16)
            opcao = int(input('Qual a sua opção: '))
            print('=-=' * 16)
            sleep(2)
            if opcao == 1:
                saldo = 3000 - 10
                print('SAQUE R$ 10.00 EFETUADO COM SUCESSO!'
                      '')
                sleep(2)
                print(f'SALDO ATUAL DISPONIVEL PARA SAQUUE R$ {saldo:.2f}')
                print('=-='* 16)
                sleep(3)
            elif opcao == 2:
                saldo = 3000 - 20
                print('SAQUE R$ 20.00 EFETUADO COM SUCESSO!'
                      '')
                sleep(2)
                print(f'SALDO ATUAL DISPONIVEL PARA SAQUUE R$ {saldo:.2f}')
                print('=-=' * 16)
                sleep(3)
            elif opcao == 3:
                saldo = 3000 - 40
                print('SAQUE R$ 40.00 EFETUADO COM SUCESSO!'
                      '')
                sleep(2)
                print(f'SALDO ATUAL DISPONIVEL PARA SAQUUE R$ {saldo:.2f}')
                print('=-=' * 16)
                sleep(3)
            elif opcao == 4:
                saldo = 3000 - 50
                print('SAQUE R$ 50.00 EFETUADO COM SUCESSO!'
                      '')
                sleep(2)
                print(f'SALDO ATUAL DISPONIVEL PARA SAQUUE R$ {saldo:.2f}')
                print('=-=' * 16)
                sleep(3)
            elif opcao == 5:
                saldo = 3000 - 100
                print('SAQUE R$ 100.00 EFETUADO COM SUCESSO!'
                      '')
                sleep(2)
                print(f'SALDO ATUAL DISPONIVEL PARA SAQUUE R$ {saldo:.2f}')
                print('=-=' * 16)
                sleep(3)
            elif opcao == 6:
                saldo = 3000 - 300
                print('SAQUE R$ 300.00 EFETUADO COM SUCESSO!'
                      '')
                sleep(2)
                print(f'SALDO ATUAL DISPONIVEL PARA SAQUUE R$ {saldo:.2f}')
                print('=-=' * 16)
                sleep(3)
            elif opcao == 7:
                saldo = 3000 - 600
                print('SAQUE R$ 600.00 EFETUADO COM SUCESSO!'
                      '')
                sleep(2)
                print(f'SALDO ATUAL DISPONIVEL PARA SAQUUE R$ {saldo:.2f}')
                print('=-=' * 16)
                sleep(3)
            elif opcao == 8:
                saldo = 3000 - 1000
                print('SAQUE R$ 1.000,00 EFETUADO COM SUCESSO!'
                      '')
                sleep(2)
                print(f'SALDO ATUAL DISPONIVEL PARA SAQUUE R$ {saldo:.2f}')
                print('=-=' * 16)
                sleep(3)
            elif opcao == 9:
                saque = float(input('INFORME O VALOR DO SAQUE R$ '))
                if saque <= 3000:
                    saldo = 3000 - saque
                    print('{:^16}'.format(f'SAQUE R$ {saque:.2f} EFETUADO COM SUCESSO!'))
                    print('=-=' * 16)
                    sleep(2)
                    print(f'SALDO ATUAL DISPONIVEL PARA SAQUUE R$ {saldo:.2f}')
                    print('=-='*16)
                    sleep(3)
                else:
                    print('{:^16}'.format(f'VALOR INDISPONÍVEL PARA SAQUE!!'))
                    print(f'TENTE NOVAMENTE!')
                    print('=-=' * 16)
                    sleep(3)
                    saque2 = float(input('INFORME O VALOR DO SAQUE R$ '))
                    if saque2 <= 3000:
                        saldo2 = 3000 - saque2
                        print('{:^16}'.format(f'SAQUE R$ {saque2:.2f} EFETUADO COM SUCESSO!'))
                        print('=-=' * 16)
                        sleep(2)
                        print(f'SALDO ATUAL DISPONIVEL PARA SAQUUE R$ {saldo2:.2f}')
                        print('=-=' * 16)
                        sleep(3)
                    else:
                        print('{:^16}'.format(f'VALOR INDISPONÍVEL PARA SAQUE!!'))
                        print(f'TENTE NOVAMENTE MAIS TARDE...')
                        print('=-=' * 16)
                        sleep(2)
                        print('FINALIZANDO O PROGRAMA...')
                        print('=-=' * 16)
                        sleep(3)
                        print('{:^16}'.format('PROGRAMA FINALIZADO COM SUCESSO!'))
                        print('{:^16}'.format('VOLTE SEMPRE AO BANCO ARC - CARVALHO!'))
                        print('{:^36}'.format('Tenha um Bom Dia!'))
                        print('=-=' * 16)
                        break
                sleep(3)
            else:
                print('Opção Inválida! Tente novamente!')
                print('=-=' * 16)
                sleep(2)
            sleep(3)
            break
    if opcao == 3:
        deposito = float(input('INFORME O VALOR DO DEPÓSITO R$ '))
        saldo = 3000 + deposito
        print('{:^16}'.format(f'DEPÓSITO DE R$ {deposito:.2f} - EFETUADO COM SUCESSO!'))
        print('=-='* 16)
        sleep(3)
        print(f'SALDO ATUAL PARA SAQUE R$ {saldo:.2f}')
        print('=-='*16)
        sleep(3)
        resposta2 = ' '
        while resposta2 not in 'S/N':
            resposta2 = str(input('DESEJA REALIZAR UM NOVO DEPÓSITO? [S/N] >> ')).strip().upper()[0]
            print('=-=' * 16)
            if resposta2 == 'N':
                print('{:^16}'.format('FINALIZANDO PROGRAMA...'))
                print('=-='* 16)
                sleep(3)
                break
            if resposta2 == 'S':
                deposito2 = float(input('INFORME O VALOR DO DEPÓSITO R$ '))
                saldo3 = 3000 + deposito2
                print('=-=' * 16)
                sleep(2)
                print(f'DEPÓSITO DE R$ {deposito2:.2f} - EFETUADO COM SUCESSO!')
                print('=-='* 16)
                sleep(2)
                print(f'Saldo atual Disponivel R$ {saldo3:.2f}')
                sleep(3)
                print('FINALIZANDO O PROGRAMA...')
    else:
        sleep(2)
        print('{:^16}'.format('FINALIZANDO O PROGRAMA...'))
        sleep(3)
    break
print('=-='*16)
sleep(3)
print('{:^16}'.format('PROGRAMA FINALIZADO COM SUCESSO!'))
print('{:^16}'.format('VOLTE SEMPRE AO BANCO ARC - CARVALHO!'))
print('{:^36}'.format('Tenha um Bom Dia!'))
print('=-='*16)