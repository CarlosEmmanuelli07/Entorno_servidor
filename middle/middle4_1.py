##  4. Filtra una lista de edades para quedarte con los mayores de edad.
l = [10, 15, 18, 20, 12, 4, 20, 35, 60]

## declaramos la funcion
def GetOlder(element):
    return element >= 18

l2 = filter(GetOlder, l)
print(list(l2))