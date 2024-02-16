print('='*36)
print('{:^36}'.format('BANCO ARC - CARVALHO'))
print('='*36)
saque = float(input('VALOR DO SAQUE R$ '))
total = saque
cedula = 50
TotCedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        TotCedulas += 1
    else:
        if TotCedulas > 0:
            print(f'Total de {TotCedulas} cédulas de R$ {cedula}')
        if TotCedulas > 0:
            print(f'Total de {TotCedulas} CÉDULAS DE R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 2
        TotCedulas = 0
        if total == 0:
            break
print('='*36)
print(f'VOLTE SEMPRE AO BANCO ARC - CARVALHO!')
print('{:^36}'.format('Tenha um Bom Dia!'))
print('='*36)
