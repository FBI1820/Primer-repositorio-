# ejer 6
import re

def copiar_lineas_filtradas():
    try:
        with open("datos.txt", "r", encoding="utf-8") as entrada, \
             open("filtrado.txt", "w", encoding="utf-8") as salida:

            for linea in entrada:
                numeros = re.findall(r'\d+', linea)
                if any(int(n) > 100 for n in numeros):
                    salida.write(linea)
        print("Se creó el archivo 'filtrado.txt' con las líneas filtradas.")
    except FileNotFoundError:
        print("El archivo 'datos.txt' no fue encontrado.")
copiar_lineas_filtradas()

