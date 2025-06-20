# ejer 3:Realice un programa que pida al usuario el nombre o ubicación de un archivo de texto
# y, a continuación añada texto en él hasta que el usuario lo decida.
nombre_archivo = input("Ingrese el nombre para el siguiente archivo: ")

with open(nombre_archivo, 'a') as archivo:
    while True:
        texto = input("Añadir cant de texto al archivo (o escriba 'fin' para terminar): ")
        if texto.lower() == 'fin':
            break
        archivo.write(texto + '\n')

print("Texto añadido al archivo correspondiente.")
