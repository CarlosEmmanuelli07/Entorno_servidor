print("Introduce un numero")
n = int(input())

def es_primo(n):
    for i in range(2, n):
        if (n % i) == 0:
            print("No es primo")
            break
        else:
            print("Es primo")
            break
es_primo(n)