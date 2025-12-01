#Esteban Muñoz, Abdiel Torrealba y Brayan Torres
# 3°D
#14/11/25

# Define la funcion
def productoMasCaro(productos):

  # Es donde se guarda el nombre del producto mas caro, que no tiene ningun nombre
    productoCaro = None

    # Esta es donde se guarda el precio mas alto
    PrecioMaximo = 0


    # Recorre cada linea del archivo
    for linea in productos:

      # Elimina los espacio y los separa por una ","
        partes = linea.strip().split(',')

        # Aqui es donde se comprueba que el archivo tenga 4 partes
        if len(partes) == 4:

          #Guarda el nombre del producto
            nombre_producto = partes[1].strip()

            # Guarda el precio y lo tranforma para poder compararlo
            precio_producto = float(partes[2].strip())


            #En esta funcion es donde actualizamos los precio del maximo, recorriendo todos los productos
            if precio_producto > PrecioMaximo:
              PrecioMaximo = precio_producto
              productoCaro = nombre_producto



    #Devuelve el nombre del producto mas caro
    return productoCaro


# Abre el archivo en modo lectura
with open('productos.csv', 'r') as archivo:
    productos = archivo.readlines()
# Llama a la funcion ya creada anteriormente
producto_caro = productoMasCaro(productos)

# Te imprime el resultado
if producto_caro:
    print(f"El producto más caro es: {producto_caro}")
else:
    print("No se encontró un producto válido.")





import csv

def valorTotalBodega(productos):
    lector = csv.reader(productos)
    #next(lector)  # saltar la cabecera si existe
    total = 0
    for fila in lector:
        # Suponemos que el archivo tiene: nombre, precio, cantidad
        id, nombre, precio, cantidad = fila
        total += float(precio) * int(cantidad)
    print(f"El valor total en bodega es: ${total:,.2f}")
    return total


# Se abre el archivo y se llama a la función que crearon
with open('productos.csv', 'r', newline='', encoding='utf-8') as productos:
    valorTotalBodega(productos)






def ProductosMayorIngresos(productos, items):
    # Diccionarios para almacenar los precios y nombres de los productos
    precios = {}
    nombres = {}

    # Cargar productos y precios
    for linea in productos:

      # es la manera en la que separa las cosas
        partes = linea.strip().split(',')

        # te cuenta las parte que tiene el archivo
        if len(partes) == 4:

          # es el lugar donde se encuentra el id
            id_producto = partes[0]

            # lugar donde se encuentra el producto
            nombre_producto = partes[1]

            #lugar donde se encuentra el precio
            precio = float(partes[2])

            # Saca el precio del archivo y lo guarda en el diccionario "precios", lo mismo pasa con el nombre
            precios[id_producto] = precio
            nombres[id_producto] = nombre_producto

    # Diccionario para almacenar los ingresos generados por cada producto
    ingresos = {}

    # Calcular los ingresos por cada producto
    for linea in items:

      # es la manera que separa las cosas
        partes = linea.strip().split(';')

        # Te cuenta las parte que tiene el archivo
        if len(partes) == 3:

          # es el lugar donde se encuentra el id
            id_producto = partes[1]

            # es el lugar donde se encuentra la cantidad
            cantidad = int(partes[2])

            #
            if id_producto in precios:
                precio = precios[id_producto]
                ingreso_producto = precio * cantidad

                if id_producto in ingresos:
                    ingresos[id_producto] += ingreso_producto  # Acumula los ingresos
                else:
                    ingresos[id_producto] = ingreso_producto  # Si es el primer ingreso, lo asigna


    # Si no se encontraron ingresos, devolver un mensaje
    #if not ingresos:
    #    return "No se encontraron ingresos."

    # Encontrar el producto con los mayores ingresos
    id_max = max(ingresos, key=ingresos.get)

    # Devolver el nombre del producto con más ingresos
    return nombres[id_max]

# Ejemplo de uso
with open('productos.csv', 'r') as productos:
    with open('items.csv', 'r') as items:
        print(ProductosMayorIngresos(productos, items))
