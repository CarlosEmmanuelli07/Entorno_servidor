# Solicitamos numeros al usuario
print("Introduce un numero")
numero1 = int(input())
print("Introduce un numero")
numero2 = int(input())

# realizamos las comprobaciones
if numero1 > numero2:
    print(numero1, " es mayor que ", numero2)
else:
    print(numero2, " es mayor que ", numero1)