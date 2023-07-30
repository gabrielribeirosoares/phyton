import math
from math import (sin, cos, tan)
a = float(input('Digite um valor para o ângulo: '))
seno = sin(math.radians(a))
cos = cos(math.radians(a))
tan = tan(math.radians(a))
print('O ângulo de {} para seno é {:.2f}, cosseno é {:.2f} e tangente é {:.2f}'.format(a, seno, cos, tan))