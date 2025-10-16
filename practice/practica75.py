option = 0


def modify_price(key):
    if key in d:
        price = float(input("Introduce la modificación del precio:"))
        d[key] = price
        print("El valor actual del producto ", key, " es: ", price)
    else:
        print("El producto introducido no está en stock")

def erase_products(key):
    if key in d:
        d.pop(key)
        print("Producto eliminado")
    else:
        print("El producto introducido no existe")

def check_prices(d):
    d.items()
print("a")
d = {"pan": 2.5, "huevos": 4.20, "cereales":2.4, "jamon": 7.9}


while option < 4:
    option = int(input("Introduce una numero del 1 al 4" \
    "\n1- Modificar precio" \
    "\n2- Eliminar producto" \
    "\n3- consultar precios y productos" \
    "\n4- Salir: \n"))
    key = str(input("Introduce el nombre de un producto: "))
    match option:
        case 1:
            modify_price(key)
        case 2:
            erase_products(key)
        case 3:
            check_prices(d)
        case 4:
            break