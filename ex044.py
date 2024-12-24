print('='*10, 'Loja Almarke', '='*10)
preco = float(input('O preço da comopra: R$ '))
print('FORMA DE PAGAMENTO')
print('[ 1 ] à vista dineiro/PIX')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2X no cartão')
print('[ 4 ] 3X no cartão')

opcao = int(input('Qual a opção? '))

if opcao == 1:
    print(f'Sua compra é de R$ {preco:.2f}, vai custar R$ {preco - (preco * 0.1)} no final')
elif opcao == 2:
    print(f'Sua compra é de R$ {preco:.2f}, vai custar R$ {preco * 0.05} no final')
elif opcao == 3:
    print(f'Sua compra é de R$ {preco:.2f}, vai custar R$ {preco} no final')
elif opcao == 4:
    print(f'Sua compra é de R$ {preco:.2f}, vai custar R$ {(preco * 0.2) + preco} no final')
else:
    print('Não tem essa opção, tente novamente.')
