#ejer 2 Contador de Líneas
#• Problema: Desarrolla un programa que pida al usuario el nombre de un archivo de texto. El
#programa deberá leer el archivo y mostrar en pantalla el número total de líneas que contiene.
#Debe manejar el error en caso de que el archivo no exista. 
nombre_archivo = input("Ingresar nombre del siguiente archivo (Elpoema.txt): ")

try:
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()
        print(f"El archivo tiene {len(lineas)} líneas.")
except FileNotFoundError:
    print("Error: El archivo no existe. Verifica el nombre o la ubicación.")
