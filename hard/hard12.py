print("Introduce la nota")
nota = float(input())

#creamos la funcion
def calificacion(nota):
    if nota < 0:
        print("Lerdo pon positivos no negativos")
    if nota >= 0 and nota < 5:
        print("Suspenso")
    if nota >= 5 and nota < 7:
        print("Aprovado")
    if nota >= 7 and nota < 9:
        print("Notable")
    if nota >=9 and nota <= 10:
        print("Sobresaliente")
calificacion(nota)