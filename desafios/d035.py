print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1+n2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os elementos acima NÃO PODEM formar um triângulo!')
