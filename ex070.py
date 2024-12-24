print('-' * 50)
print('LOJA SUPER BARATÃO')
print('-' * 50)

menor = 0
maior = 0
total = 0
produto_mais_barato = ''
cont = 'S'

while cont == 'S':
    nome = input('Nome do Produto: ').strip()
    preco = float(input('Preço: R$ '))

    total += preco

    if preco > 1000:
        maior += 1

    if menor == 0 or preco < menor:
        menor = preco
        produto_mais_barato = nome

    cont = input('Quer continuar? [S/N] ').strip().upper()
    while cont not in 'SN':
        cont = input('Resposta inválida. Quer continuar? [S/N] ').strip().upper()

print('-' * 50)
print('FIM DO PROGRAMA')
print('-' * 50)
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {maior} produto(s) custando mais de R$ 1000.00')
print(f'O produto mais barato foi "{produto_mais_barato}" que custa R$ {menor:.2f}')

