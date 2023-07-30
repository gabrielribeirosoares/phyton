from math import hypot
ca = float(input('Cateto adjacente: '))
co = float(input('Cateto oposto: '))
hip = hypot(ca, co)
print('A hipotenusa vai medir {:.2f}'.format(hip))