valor = float(input('Primeiro valor: '))
valor2 = float(input('Segundo valor: '))
opcao = True
while opcao:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    opcao = int(input('Qual é a opção? '))
    if opcao == 1:
        soma = valor + valor2
        print(f'A soma de {valor} e {valor2} é {soma}')
    elif opcao == 2:
        multiplicacao = valor * valor2
        print(f'A multiplicação de {valor} e {valor2} é {multiplicacao}')
    elif opcao == 3:
        if valor > valor2:
            print(f'O {valor} é maior que {valor2}')
        elif valor < valor2:
            print(f'O {valor2} é maior que {valor}')
        else:
            print(f'O {valor2} é igual a {valor}')
    elif opcao == 4:
        print('Infome os números novamente')
        valor = float(input('Primeiro valor: '))
        valor2 = float(input('Segundo valor: '))
    elif opcao == 5:
        opcao = False
    else:
        print('Opção invalida. Tente novamente')
    print('=-'*20)
print('Finalizado o programa')
