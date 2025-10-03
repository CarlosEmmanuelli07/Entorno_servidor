print("Introduce la cantidad de euros.")
euros = float(input())

def euros_a_centimos(euros):
    cents = euros * 100
    print("tienes ", cents, " centimos")

euros_a_centimos(euros)