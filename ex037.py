v = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')

opcao = int(input('Sua opção: '))


if opcao == 1:
    print(f'{v} convertido para BINÁRIO é igual a {bin(v)}')
elif opcao == 2:
    print(f'{v} convertido para OCTAL é igual a {oct(v)}')
elif opcao == 3:
    print(f'{v} convertido para OCTAL é igual a {hex(v)}')
else:
    print('Opção inválida. Tente novamente.')
