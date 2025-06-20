#ejer 5

import re

def contar_lineas(archivo):
    """Cuenta el número total de líneas en el archivo."""
    lineas = archivo.readlines()
    return len(lineas)

def contar_palabras(linea):
    """Cuenta palabras en una línea (usando regex para precisión)."""
    return len(re.findall(r'\b\w+\b', linea))

def contar_python(linea):
    """Busca la palabra 'python' (case-insensitive y como palabra completa)."""
    return len(re.findall(r'\bpython\b', linea.lower()))

def estadisticas_texto():
    """Función principal que calcula y muestra las estadísticas del archivo."""
    try:
        with open("texto.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            total_lineas = len(lineas)
            total_palabras = 0
            conteo_python = 0
            
            for linea in lineas:
                total_palabras += contar_palabras(linea)
                conteo_python += contar_python(linea)
            
            print(f"Total de líneas: {total_lineas}")
            print(f"Total de palabras: {total_palabras}")
            print(f"Veces que aparece 'Python': {conteo_python}")
    
    except FileNotFoundError:
        print("Error: Archivo 'texto.txt' no encontrado.")
    except Exception as e:
        print(f"Error inesperado: {e}")
if __name__ == "__main__":
    estadisticas_texto()
