# Ejercicio 1
nombre_archivo = input("Ingrese el nombre del archivo para guardar frases ( frases de usuario.txt): ")

with open(nombre_archivo, 'w') as archivo:
    while True:
        frases = input("Escriba una frase (o escriba 'fin' para terminar): ")
        if frases.lower() == 'fin':
            break
        archivo.write(frases + '\n')

print("Frases guardadas correctamente en el archivo.")
