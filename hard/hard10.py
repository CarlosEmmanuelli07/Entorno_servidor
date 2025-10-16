print("Introduce un numero.")
n = int(input())

def signo(n):
    if n > 1:
        print("Es positivo")
    elif n == 0:
        print("Es igual a 0")
    else:
        print("Es negativo")

signo(n)