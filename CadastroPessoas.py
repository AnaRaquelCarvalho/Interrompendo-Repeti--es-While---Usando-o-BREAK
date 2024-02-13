print('=-='*14)
print(f'        Cadastro de Pessoas        ')
print('=-='*14)
tot18 = tothomens = totMulheres20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        tothomens += 1
    if sexo == 'F' and idade < 20:
        totMulheres20 += 1
    resp = ' '
    print('=-='*14)
    while resp not in 'SN':
        resp = str(input('Quer Continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
    print('=-='*14)
print(f'Total de pessoas maiores de 18 anos: {tot18}')
print(f'Ao todo foram {tothomens} homens cadastrados')
print(f'Temos {totMulheres20} mulheres com menos de 20 anos')
print('=-='*14)