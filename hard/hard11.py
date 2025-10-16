print("Introduce un año")
anio = int(input())

# creamos la función
def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        print("Es visiesto")
    else:
        print("No es visiesto")

es_bisiesto(anio)
