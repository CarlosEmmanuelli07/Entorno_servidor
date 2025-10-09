##  Se solicita nombres de personas que entran al edificio.
print("Introduce el nombre de los inquilinos")
Tenants = []
name = " "
duplicados = 0
unicos = 0

## Realizamos un set para almacenarlos.
while True:
    name = str(input()).strip() ## Evita espacios vacíos
    if name.lower() == "fin":
        break    
    Tenants.append(name)

## Mostrar los repetidos
unicos = len(set(Tenants))
print(unicos)

duplicados = [n for n in set(Tenants) if Tenants.count(n) > 1]
print(f"Nombres repetidos: {len(duplicados)}")
if duplicados:
    print("Se repiten:", ", ".join(duplicados)) ## join une todos los string en un unico string 
else:
    print("No hay duplicados")
