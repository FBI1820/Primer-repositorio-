# ejer 1 Diario Personal
#Problema: Escribe un programa que funcione como un diario simple. Cada vez que se ejecute, debe solicitar
#  al usuario una entrada de texto y la guardará, junto con la fecha y hora actual, en un archivo llamado diario.txt. 
# Cada nueva entrada debe añadirse al final del
#archivo sin borrar las anteriores.


import datetime  # Asegúrate de importar correctamente

entrada = input("Escribir entrada de tu diario: ")

fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("diario.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"{fecha_hora} - {entrada}\n")

print("Se guardado de forma exitosa a 'diario.txt'.")
