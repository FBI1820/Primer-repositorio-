#Trabajando con archivos de texto en Python

 #1. Abrir el archivo en modo creación


#Ejemplo, solicitando el nombre del archivo al usuairo

ruta=input("Nombre del archivo:")

archi1=open(ruta, 'a')

#archi1.write("Primera linea \n")

archi1.write("Segunda linea \n")
archi1.write("Tercera linea \n")
archi1.close()

print("Fin del programa")