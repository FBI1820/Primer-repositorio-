#Filtrado de líneas que contienen una palabra específica: Escribe un programa que lea un archivo “libro.txt” y cree un
# nuevo archivo “filtrado.txt”
# que solo contenga las líneas que tienen una palabra específica proporcionada por el usuario.
palabra=input("Ingrese la palabra a buscar: ")  
lineas_filtradas = []
with open("libro.txt", "r", encoding='utf-8') as archivo:
    for lineas in archivo:
        if palabra in lineas:
            lineas_filtradas.append(lineas)
with open("filtrado.txt", "w", encoding='utf-8') as archivo_salidas:
    for lineas in lineas_filtradas:
        archivo_salidas.write(lineas)
        
print("Las lineas filtradas se ha guardado en 'filtrado.txt'")