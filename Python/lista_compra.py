# Importar cosas. NLTK es una librería estandar de procesar textos. Es el seat ibiza del lenguaje natural, no acapara titulares pero vale para todo.

import nltk
from nltk.corpus import stopwords


# Primero nos descargamos la puntuación y las palabras de relleno. Si ya las tenemos no se descargan.

nltk.download("punkt")
nltk.download("stopwords")
stops = set(stopwords.words("spanish")) # Poner las de español. Asumimos que no hay selección de idioma pero sería trivial.

# Ahora me invento una lista de la compra. 3 productos que existen y 1 que no.
# Asumo que la interfaz guarda la lista en un diccionario. Porque puedo. Pero puede ser una lista de tuplas, o un df si importamos pandas.
# También asumo que al generar el diccionario, la primera letra va con mayúsucula y el resto en minúscula, y sin faltas de ortografía.
# El diccionario guarda la clave, que es una palabra o varias y un valor, que es la cantidad.
# La cantidad es un entero, en mi supermercado no se puede comprar 1kg de patatas sino que hay que contarlas.

dict_lista_compra = {"Yogures": "6", "Cerveza": "24", "Queso": "1", "jkjjadsj": "1"} # Esto es lo que el usuario quiere comprar.

# Ahora tengo una base de datos con todos los productos del supermercado. Voy a poner 6, los 3 que tenemos en la lista de la compra y otros que no.
# No me meto en temas de ortografía. Los productos están guardados con la misma clave que el usuario va a poner en la lista.
# El diccionario guarda la clave, que es una palabra o varias y un valor, que es el precio por unidad. Si compro 6 yogures, el precio será 6 * 1.05 euros. Cómo está la inflación!

dict_bd_productos = {"Yogures": "1.05", "Cerveza": "3.25", "Queso": "5.6", "Donuts": "0.80", "Pollo": "5.25", "Jamón": "15.6"}

# Ahora busco la intersección de mi lista de la compra con los productos del supermercado.
# Si tiene los productos, se imprime el producto, el precio unitario y el precio total.
# Si no tiene los productos, se imprime que no tiene ese producto.

#print(dict_lista_compra.keys())

dict_productos_para_comprar = {} # Diccionario vacío para añadir los productos que el usuario va a comprar
dict_productos_no_encontrados = {} # Diccionario vacío para añadir los productos de la lista de la compra que el supermercado no tiene

for elem in dict_lista_compra.keys():
    if elem in dict_bd_productos.keys():
        precio_unitario = float(dict_bd_productos[elem])
        cantidad_producto = int(dict_lista_compra[elem])
        precio_total = round(precio_unitario * cantidad_producto, 2)
        print(precio_total)
        dict_productos_para_comprar[elem] = [elem, cantidad_producto, precio_unitario, precio_total]



print(dict_productos_para_comprar)

# Ahora tengo que poner otro diccionario con las claves y una lista, precio unitario, total y cantidad
# Y luego capturar los productos que no están


