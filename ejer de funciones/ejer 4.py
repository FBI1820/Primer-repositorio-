#ejer 4
# Paso 1 y 2: Registrar estudiantes y guardar en archivo
def registrar_estudiantes():
    cantidad = int(input("¿Cuántos estudiantes deseas ingresar? "))
    with open("estudiantes.txt", "w") as archivo:
        for i in range(cantidad):
            nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
            promedio = float(input(f"Ingrese el promedio de {nombre}: "))
            archivo.write(f"{nombre},{promedio}\n")
    print("Datos guardados en estudiantes.txt\n")

# Paso 3 y 4: Leer archivo, contar y mostrar aprobados
def contar_y_mostrar_aprobados():
    aprobados = []
    try:
        with open("estudiantes.txt", "r") as archivo:
            for linea in archivo:
                nombre, promedio = linea.strip().split(",")
                if float(promedio) >= 70:
                    aprobados.append((nombre, float(promedio)))

        if aprobados:
            print(f" Total de estudiantes que aprobaron: {len(aprobados)}")
            print("Lista de aprobados:")
            for nombre, promedio in aprobados:
                print(f"- {nombre} con promedio {promedio:.2f}")
        else:
            print("Ningún estudiante aprobó.")

    except FileNotFoundError:
        print("El archivo estudiantes.txt no existe. Primero registra estudiantes.")

# Programa principal
def main():
    registrar_estudiantes()
    contar_y_mostrar_aprobados()
main()
