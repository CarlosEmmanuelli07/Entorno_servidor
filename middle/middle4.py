## 4. Usa map para calcular la longitud de cada palabra de una lista.
l = ["paco", "pedro", "piolin", "manolo"]

## Realizamos una funcion para contar las letras de las palabras
def Getsize(element):
    return len(element)

## Realizamos el map y lo convertimos en listas.
l2 = map(Getsize, l)
print(list(l2))