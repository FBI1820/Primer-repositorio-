#ejer 4
import os

nombre_archivo = "productos.csv"

# Crear archivo de ejemplo solo si no existe
if not os.path.exists(nombre_archivo):
    datosdeejemplo = [
        "Laptop,1200,15",
        "Mouse,25,50",
        "Teclado,75,30"
    ]
    
    with open(nombre_archivo, "w") as archivo:
        for linea in datosdeejemplo:
            archivo.write(linea + "\n")
    print(f"Se ha creado el archivo {nombre_archivo} con datos de ejemplo.")

# Procesar el archivo (igual que la versión corregida anterior)
try:
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            datos = linea.split(',')
            if len(datos) == 3:
                nombre, precio, stock = datos
                print(f"Producto: {nombre} | Precio: ${precio} | Stock: {stock} unidades")



except FileNotFoundError:
    print("Error: No se encontró el archivo 'productos.csv'")
