#Realice un programa que pida al usuario 
#el nombre de un archivo de texto y, 
#a continuación permita almacenar al usuario tantas frases como el usuario desee.
print("crear nombre del archivo")
nombre_archivo=input("ingrese el nombre al archivo")
texto= input("ingresar multiples frases")
with open("texto.txt",'w') as archivo:
    archivo.write(texto)

with open ("texto.txt", 'a') as archivo: 
    archivo.write(texto)