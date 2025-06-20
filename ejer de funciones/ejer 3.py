#Ejercicio 3: Validación de contraseña
#Problema:
#Desarrolla un programa que valide una contraseña según los siguientes criterios: mínimo 8 caracteres, al menos una mayúscula, un número y un carácter especial. Usar funciones para cada validación.

import string

def tiene_mayuscula(contra):
    return any(c.isupper() for c in contra)
def tiene_numero(contra):
    return any(c.isdigit() for c in contra)
def tiene_especial(contra):
    especiales = string.punctuation  
    return any(c in especiales for c in contra)
def tiene_longitud(contra):
    return len(contra) >= 8

def validar_contrasena(contra):
    errores = []

    if not tiene_longitud(contra):
        errores.append("tener minimo de 8 caracteres.")
    if not tiene_mayuscula(contra):
        errores.append("Debe tener al menos una letra mayúscula.")
    if not tiene_numero(contra):
        errores.append("Debe tener al menos un número.")
    if not tiene_especial(contra):
        errores.append("Debe tener al menos un carácter especial.")

    if not errores:
        print("Contraseña válida.")
    else:
        print("Contraseña inválida por las siguientes razones:")
        for error in errores:
            print("-", error)
def main():
    contra = input("Ingresa tu contraseña: ")
    validar_contrasena(contra)

main()