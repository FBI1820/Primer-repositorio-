#ejer 4: 
#Lector de Datos CSV
#• Problema: Se proporciona un archivo productos.csv donde cada línea contiene el nombre
#de un producto, su precio y la cantidad en stock, separados por comas (Laptop,1200,15).
#para el usuario, indicando el nombre, precio y stock de cada producto.
try:
    with open("productos.csv", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            datos = linea.split(",")
            if len(datos) == 3:
                nombre, precio, stock = datos
                print(f"Producto: {nombre} | Precio: {precio} | Stock: {stock} unidades")

except FileNotFoundError:
    print("Error: No se encontró el archivo 'productos.csv'.")