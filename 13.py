# Solicitamos un numero al usuario
print("Introduce un numero")
num = int(input())
fact = 1

#realizamos el bucle
for i in range(1, num +1):
    fact = i * fact
    print(fact)