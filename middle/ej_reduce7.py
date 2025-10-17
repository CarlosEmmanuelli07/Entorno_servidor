## Importamos el paquete de reduce y declaramos las variables.
from functools import reduce;
inicial_num = 1
n = 7
l = range(inicial_num, n)

##realizamos la función del factorial
def factorial(n, i):
    return n * i;

l4 = reduce(factorial, l)
print(l4)