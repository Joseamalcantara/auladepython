print('-' * 40)
print(' ' * 5, '-Trabalhando com operadores-')
print('-' * 40)
print('Operadores Aritméticos')
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
soma = num1 + num2  # Usamos o sinal de "+" para somar;
diferenca = num1 - num2  # Usamos o sinal de "-" para calcular a difenrença;
produto = num1 * num2  # Usamos o simbolo "*" para para multiplicação;
divisao = num1 / num2  # Usamos o simbolo de "/" para divisão;
divisaointeira = num1 // num2  # Usamos o simbolo de "//" para a parte inteira da divisão;
resto = num1 % num2  # Usamos o simbolo de "%" para saber o reso da divisão
exponencial = num1 ** num2  # Usamos os simbolos "**" para calculos exponeciais
print(f'A soma de {num1} e {num2} é {soma}')
print(f'A diferença de {num1} e {num2} é {diferenca}')
print(f'O produto de {num1} e {num2} é {produto}')
print(f'A divisão de {num1} e {num2} é {divisao:.1f}')
print(f'A divisão inteira de {num1} e {num2} é {divisaointeira}')
print(f'O resto da divisão de {num1} e {num2} é {resto}')
print(f'Com a base {num1} e o expoente {num2} o resultado é {exponencial}')
