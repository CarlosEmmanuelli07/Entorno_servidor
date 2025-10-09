## Creamos la funcion.
def type_phrase():

    ## Se solicuitan los datos al usuario y declaramos las variables.
    print("Introduce una frase.")
    phrase = str(input())

    ## Empezamos a contar aparece una vocal
    n_a = phrase.count('a')
    print("Letra a: ", n_a)
    n_e = phrase.count('e')
    print("Letra e: ", n_e)
    n_i = phrase.count('i')
    print("Letra i: ", n_i)
    n_o = phrase.count('o')
    print("Letra o: ", n_o)
    n_u = phrase.count('u')
    print("Letra u: ", n_u)

    print(phrase[::-1])