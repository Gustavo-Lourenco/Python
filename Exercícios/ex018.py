import math

a = float(input('Digite o valor do ângulo: '))
print('Para o ângulo de {}º\nO cosseno é {:.3f}\nO seno é {:.3f}\nA tangente é {:.3f}'.format(a, math.cos(math.radians(a)), math.sin(math.radians(a)), math.tan(math.radians(a))))
