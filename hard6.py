print("dame un numero.")
num1 = int(input())
print("dame un numero.")
num2 = int(input())

def maximo(num1, num2):
    if num1 > num2:
        print(num1 ," es mayor que ", num2)
    else:
        print(num2 ," es mayor que ", num1)
maximo(num1, num2)