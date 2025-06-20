#ejemplo 1 de archivos 
 
archi1=open("datos.txt",'a')
archi1.write("primera linea \n")
archi1.write("segunda linea \n")
archi1.write("tercera linea \n")
archi1.close()
archi1=open("datos.txt",'r')
contenido=archi1.read()
print (contenido)
archi1.close()
print ("fin del programa")  