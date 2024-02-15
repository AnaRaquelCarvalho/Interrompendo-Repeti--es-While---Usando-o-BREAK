print('=-='*14)
print(f'        Cadastramento de Pessoas        ')
print('=-='*14)
TotalCadastrados = 0
IdadeMaior = IdadeMenor = 0
Homens = Mulheres = 0
while True:
    idade = int(input('Idade: '))
    TotalCadastrados += 1
    sexo =' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        IdadeMaior += 1
    if idade < 18:
        IdadeMenor += 1
    if sexo == 'M':
        Homens += 1
    if sexo == 'F':
        Mulheres += 1
    resp = ' '
    print('=-='*14)
    while resp not in 'SN':
       resp = str(input('Quer Continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
    print(f'=-='*14)
print((((f'Total de pessoas registradas: {TotalCadastrados}\n'
         f'Maiores de 18 anos: {IdadeMaior}\n'
         f'Menores de 18 anos: {IdadeMenor}\n'
         f'Total de Homens: {Homens}\n'
         f'Total de Mulheres: {Mulheres}'))))