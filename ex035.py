print('-='*20)
print('Analisandor de Triângulos')
print('-='*20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos assima PODEM FORMAR triângulos!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulos!')
