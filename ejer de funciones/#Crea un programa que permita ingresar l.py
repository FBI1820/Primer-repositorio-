#Crea un programa que permita ingresar las calificaciones de varios estudiantes y que, mediante funciones, calcule el promedio general, la calificación más alta y la más baja.
#Definir una función calcular_promedio(lista_notas) que retorne el promedio.
#2. Definir funciones nota_mayor(lista) y nota_menor(lista) para obtener el valor máximo y mínimo.
#. Pedir al usuario la cantidad de estudiantes.
# Almacenar las calificaciones en una lista. Llamar a las funciones y mostrar resultados
# Función para calcular el promedio
# Función para calcular el promedio
def calcular_promedio(cant_notas):
    return sum(cant_notas) / len(cant_notas)
def mejor nota(lista):
    return max(lista)
def peor nota (lista):
    return min(lista)
def main():
    try:
        cant_estudiantes = int(input("Cantidad de estudiantes: "))
        calificaciones = []
        for i in range(cant_estudiantes):
            nota = float(input(f"Calificación por estudiante {i + 1}: "))
            calificaciones.append(nota)
        print("\n--- Resultados ---")
        print(f"Promedio: {calcular_promedio(calificaciones):.2f}")
        print(f"Nota más alta: {nota_mayor(calificaciones)}")
        print(f"Nota más baja: {nota_menor(calificaciones)}")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")
if __name__ == "__main__":
    main()
    
    