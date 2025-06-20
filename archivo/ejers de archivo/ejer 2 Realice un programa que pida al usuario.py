#Realice un programa que pida al usuario el nombre o ubicación de un archivo de texto y, a
# continuación de lectura a todo el archivo.
nombre_archivo = input("Escriba el nombre del archivo: ")

try:
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        print("\nContenido del archivo:")
        print(contenido)
except FileNotFoundError:
    print("Archivo no encontrado.")

