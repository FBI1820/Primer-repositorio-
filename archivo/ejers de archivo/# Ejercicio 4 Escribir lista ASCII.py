# Ejercicio 4 Escribir un programa que escriba la lista de caracteres ASCII dentro de un archivo de texto.

nombre_archivo = "ascii.txt"

with open(nombre_archivo, 'w') as archivo:
    for i in range(32, 128):  # Rango visible de caracteres ASCII
        archivo.write(f"{i} -> {chr(i)}\n")

print("Archivo 'ascii.txt' creado con los caracteres ASCII.")
