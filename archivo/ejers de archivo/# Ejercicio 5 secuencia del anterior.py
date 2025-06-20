# Ejercicio 5 Escribir un programa que lea y muestre en pantalla el archivo generado
#  en el ejercicio anterior.

try:
    with open("ascii.txt", 'r') as archivo:
        contenido = archivo.read()
        print("Contenido del archivo ASCII:")
        print(contenido)
except FileNotFoundError:
    print("El archivo 'ascii.txt' no existe. Ejecuta el ejercicio anterior primero.")
