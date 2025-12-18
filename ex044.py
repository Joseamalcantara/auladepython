# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

titulo = " Loja Almarke "

print(f"{titulo.center(40, "=")}")
preco = float(input('O preço da comopra: R$ '))

print("""FORMA DE PAGAMENTO
[ 1 ] à vista dineiro/PIX
[ 2 ] à vista no cartão
[ 3 ] 2X no cartão
[ 4 ] 3X no cartão""")

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
