print('-'*54)
print('             SUPERMERCADO BARATÃO')
print('-'*54)
TotCompra = pago = troco = 0
MenorValor = cont = barato = MaiorValor = caro = 0
while True:
    produto = str(input('Produto: '))
    preco = float(input('Preço R$ '))
    cont += 1
    TotCompra += preco
    if cont == 1 or preco > MaiorValor:
        MaiorValor = preco
        caro = produto
    if cont == 1:
        MenorValor = preco
        barato = produto
    else:
        if preco < MenorValor:
            MenorValor = preco
            barato = produto
    resposta = ' '
    print('-' * 56)
    while resposta not in 'S/N':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
    print('-' * 56)
print('{:-^56}'.format(' COMPRA FINALIZADA  '))
print(f'Total de compras: R$ {TotCompra:.2f}')
pago = float(input('Valor Pago R$ '))
troco = pago - TotCompra
print(f'Troco R$ {troco:.2f}')
print(f'O produto mais caro foi a(o) {caro} que custa R$ {MaiorValor:.2f}')
print(f'O produto mais barato foi a {barato} que custa R$ {MenorValor:.2f}')
print('-'*56)