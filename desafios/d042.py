print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 == n2 == n3:
    print('Os segmentos acima formam um triângulo equilátero.')
elif n1 == n2 or n1 == n3 or n2 == n3:
    print('Os segmentos acima formam um triângulo isósceles.')
else:
    print('Os segmentos acima formam um triângulo escaleno.')