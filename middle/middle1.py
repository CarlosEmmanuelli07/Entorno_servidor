## 1. Usa filter para obtener los números pares de una lista.
l = [1, 3, 6, 7, 8, 4, 2, 10, 14, 20]

## realizar la funcion de obtener numeros pares.
def ReadEven(element):
    return element % 2 == 0

l2 = filter(ReadEven, l)
print(list(l2))


