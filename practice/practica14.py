frutas = ["Mango", "Fresa", "Tomate"]

## Solicita una fruta al usuario.
print("Introduce una fruta")
fruta_soli = str(input())

## ver si existe en la lista.
if fruta_soli in frutas:
    print("Esta en la lista")
else:
    print("No está en la lista ")