print('-'*50)
print('Sequência de Fibonacci')
print('-'*50)
termo = int(input('Até quantos termos você quer mostrar? '))
print('~'*50)
inicio = 0
proximo = 1
cont = 0
while cont <= termo:
    print(f'{inicio} -> ', end=' ')
    inicio, proximo = proximo, proximo + inicio
    cont += 1
print('FIM')
