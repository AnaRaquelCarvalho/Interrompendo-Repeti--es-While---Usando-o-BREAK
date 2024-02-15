print('-'*56)
print('      Analisador de Compras à Realizar')
print('-'*56)
TotCompra = TotMil = MenorValor = cont = barato = 0
while True:
    produto = str(input('Produto: '))
    preco = float(input('Preço R$ '))
    cont += 1
    TotCompra += preco
    if preco >= 30:
        TotMil += 1
    if cont == 1:
        MenorValor = preco
        barato = produto
    else:
        if preco < MenorValor:
            MenorValor = preco
            barato = produto
    resposta = ' '
    print('-'*56)
    while resposta not in 'S/N':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
    print('-'*56)
print('{:-^56}'.format(' FIM DA ANÁLISE '))
print(f'Total de compras: R$ {TotCompra}')
print(f'Temos {TotMil} produtos custando mais de R$ 30,00')
print(f'O produto mais barato foi a {barato} que custa R$ {MenorValor:.2f}')
print('-'*56)