frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
juntos = ''.join(palavra)
print(juntos)
inverso = ''
for letras in range(len(juntos) -1, -1, -1):
    inverso += juntos[letras]
print(f'O inverso de {juntos} é {inverso} ')
if inverso == juntos:
    print(f'Temos um palídrimo!')
else:
    print('Não temos um palíndromo!')
