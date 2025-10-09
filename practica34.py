'''34. Simula una agenda de contactos. El usuario puede introducir pares nombre-teléfono hasta escribir "fin". 
Guarda los datos en un diccionario. Al final, permite buscar el número de una persona por su nombre.'''
# Realizamos la solicitud de datos y los guardamos en el diccionario.
## Declaramos el diccionario
d = {}
print("Introduce el nombre del contacto y su numero")



#Realizamos la inserción de los datos.
while True:
    contact_name = str(input())
    if contact_name == "fin":
        break
    contact_num = str(input())
    d[contact_name] = contact_num

#Pedimos al usuario que busque un contacto.

search_name = str(input("Introduce el nombre que desee buscar: "))

if search_name in d:
    print("Si esta el nombre buscado y su numero es: ", d.get(search_name))
else:
    print("El nombre no está en el diccionario.")

