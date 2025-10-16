print("Dame un numero.")
num1 = int(input())
print("Dame un numero.")
num2 = int(input())
print("Dame un numero.")
num3 = int(input())

def promedio(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    print("El promedio de los 3 numeros es: ", average)
promedio(num1, num2, num3)