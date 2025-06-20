# ejemplo con el uso de r+
archi1=open("datos.txt" ,'r+')
contenido=archi1.read()
print (contenido)
archi1.write ("otra linea 1/n ")
archi1.write ("otra linea 2/n ")
archi1.close()
