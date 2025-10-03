#Cuenta cuantas vocales hay en una cadena introducida por el usuario

print("Introduce la cadena que desee")
cadena = str(input())

n_a = cadena.count('a')
n_e = cadena.count('e')
n_i = cadena.count('i')
n_o = cadena.count('o')
n_u = cadena.count('u')

n_vocales = n_a + n_e + n_i + n_o + n_u

print("La cadena tiene: ", n_vocales, " vocales")

## OTRA FORMA PODRIA SER

print(sum(cadena.count(v)for v in ['a', 'e', 'i', 'o', 'u']))