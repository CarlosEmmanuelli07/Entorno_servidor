print("Introduce un numero")
mes = int(input())

def dia_mes(mes):
    while mes <= 12:
        for i in range (1, 12+1):
            if (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
                print("El mes tiene 31 dias")
                break
            elif (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
                print("El mes tiene 30 dias")
                break
            else:
                print("El mes tiene 28 dias")
                break
dia_mes(mes)