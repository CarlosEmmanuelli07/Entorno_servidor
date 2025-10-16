nombre_primaria = []
nombre_secundaria = []

while True:
    nombre = input("Introduce el nombre (o 'x' para terminar): ").lower()
    if nombre == "x":
        break
    if nombre:
        nombre_primaria.append(nombre)

while True:
    nombre = input("Introduce el nombre (o 'x' para terminar): ").lower()
    if nombre == "x":
        break
    if nombre:
        nombre_secundaria = []

print()