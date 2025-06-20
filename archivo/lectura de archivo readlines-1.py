archi1=open("datos.txt",'r')
lineas=archi1.readlines()
print('el archivo tiene', len(lineas), 'lineas')
print('el cotenido del archivo')
for linea in lineas:
    print(linea, end= '')
    archi1.close()