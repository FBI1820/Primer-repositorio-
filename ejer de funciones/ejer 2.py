 #Ejercicio 2: Sistema de conversión de unidades
#Problema: Implementa un programa que, usando funciones, permita convertir entre diferentes unidades de longitud (metros, kilómetros, pies, pulgadas). El usuario selecciona la conversión deseada y proporciona el valor.
def m_a_km(m):
    return m / 1000

def m_a_pies(m):
    return m * 3.28084

def m_a_pulgadas(m):
    return m * 39.3701

def km_a_m(km):
    return km * 1000

def pies_a_m(pies):
    return pies / 3.28084

def pulgadas_a_m(pulgadas):
    return pulgadas / 39.3701
def mostrar_menu():
    print("Conversión de unidades de longitud:")
    print("1. Metros a Kilómetros")
    print("2. Metros a Pies")
    print("3. Metros a Pulgadas")
    print("4. Kilómetros a Metros")
    print("5. Pies a Metros")
    print("6. Pulgadas a Metros")
    
def main():
    mostrar_menu()
    opcion = input("Selecciona una opción (1-6): ")

    if opcion in ['1', '2', '3']:
        valor = float(input("Ingresa el valor en metros: "))
    else:
        valor = float(input("Ingresa el valor en la unidad correspondiente: "))

    if opcion == '1':
        resultado = m_a_km(valor)
        print(f"{valor} metros = {resultado:.2f} kilómetros")
    elif opcion == '2':
        resultado = m_a_pies(valor)
        print(f"{valor} metros = {resultado:.2f} pies")
    elif opcion == '3':
        resultado = m_a_pulgadas(valor)
        print(f"{valor} metros = {resultado:.2f} pulgadas")
    elif opcion == '4':
        resultado = km_a_m(valor)
        print(f"{valor} kilómetros = {resultado:.2f} metros")
    elif opcion == '5':
        resultado = pies_a_m(valor)
        print(f"{valor} pies = {resultado:.2f} metros")
    elif opcion == '6':
        resultado = pulgadas_a_m(valor)
        print(f"{valor} pulgadas = {resultado:.2f} metros")
    else:
        print("Opción no válida.")
main()

