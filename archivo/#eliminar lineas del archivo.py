#eliminar lineas del archivo 
#abrir el archivo y leer las lineas
with open ('datos.txt', 'r', encoding="utf-8") as archivo: 
  lineas=archivo.readlines()
#filtrar las lineas que no contienen "segunda linea"
lineas_filtradas= [linea for linea in lineas if linea.strip()!="segunda linea"]
#sobre escribir el archivo con las lineas filtradas 
with open ('datos.txt', 'w', encoding="utf-8") as archivo: 
    archivo.writelines(lineas_filtradas)