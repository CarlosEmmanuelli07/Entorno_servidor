## Pedimos una frase
print("Introduce una frase")
phrase = str(input())

##Transformamos la cadena a mayuscuña
upper_phrase = phrase.upper()

## Realizamos un bucle para modificar las bocales por asteriscos
for i in ["A", "E", "I", "O", "U"]:
    upper_phrase = upper_phrase.replace(i, "*")

phrase = upper_phrase
print(phrase)