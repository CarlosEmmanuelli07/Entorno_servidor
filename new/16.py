# Solicitamos un numero al usuario
print("Introduce un numero")
num = int(input())

#hacemos el buvle y comprobamos.
for i in range(1, num +1):
    if i % 2 != 0:
        print(i)
