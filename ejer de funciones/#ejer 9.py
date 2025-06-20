#ejer 9
def seleccionar_nombre():
    nombres = ["Ana", "Luis", "Carlos"]
    try:
        posicion = int(input("Ingrese la posición del nombre (0-2): "))
        if 0 <= posicion < len(nombres):
            print("Nombre seleccionado:", nombres[posicion])
        else:
            print("Posición fuera de rango.")
    except ValueError:
        print("Entrada inválida. Debe ser un número entero.")

def main():
    seleccionar_nombre()

if __name__ == "__main__":
    main()
