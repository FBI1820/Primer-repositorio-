#ejer 3 Generador de Listas de Compras
# Problema: Crea un programa que permita al usuario crear una lista de compras. El programa
#solicitará al usuario que ingrese productos uno por uno y los guardará en un archivo llamado
#compras.txt. El usuario indicará que ha terminado de añadir productos introduciendo la
#palabra "fin".

lista_compras = []
lista_porductoposible=["naranjas","melones","arroz","frijoles","leche"]

print("Ingrese los productos de su lista de compras.")
print("Escriba 'fin' cuando haya terminado.\n")

while True:
    producto = input("Producto: ")
    if producto.lower() == "fin":
        break
    lista_compras.append(producto)

with open("compras.txt", "w", encoding="utf-8") as archivo:
    for item in lista_compras:
        archivo.write(item + '\n')

print("\nLista de compras guardada en compras.txt:")
print(lista_compras)
