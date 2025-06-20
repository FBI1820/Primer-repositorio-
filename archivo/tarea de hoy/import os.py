import os
from tkinter import Menu 
ARCHIVO="estudiantes.txt"
def cargar_estudiantes(): 
    estudiantes= []
    if os.path.exists(ARCHIVO):
        with open (ARCHIVO,"r") as archivo: 
            for linea in archivo: 
                codigo, nombre, apellido, carrera= linea.strip(). split(",")
        estudiantes.append({
            "codigo": codigo, 
            "nombre": nombre,
            "apellido": apellido, 
            "carrera": carrera 
        })
        return estudiantes 
    def guardar_estudiantes(estudiantes): 
        with open (ARCHIVO, 'w') as achivo:
            for est in estudiantes: 
             linea=f"{est['codigo']}, {est['nombre']}, {est['apellido']}, {est['carrera']}\n"
             archivo.write(linea)
    def crear_estudiante(estudiantes):
        codigo= input ("codigo del estudiante: ")
        if any (est["codigo"]== codigo for est in estudiantes):
            print ("El codigo ya existe\n")
            return 
        nombre= input ("nombre: ")
        apellido= input ("apellido: ")
        carrera = input ("carrera: ")
        estudiantes.append({ 
            "codigo": codigo, 
            "nombre": nombre,
            "apellido": apellido, 
            "carrera": carrera 
            })
        guardar_estudiantes(estudiantes)
        print ("estudiantes agregado correctamente.\n")
        def mostrar_estudiantes(estudiantes): 
         if not estudiantes:
             print ("no hay estudiantes registrados.\n")
             return 
         print("\n lista de estudiantes:")
         for est in estudiantes: 
             print(f"Codigo: {est['codigo']}, Nombre: {est['nombre']}, Apellido: {est['apellido']}, Carrera:{est['carrera']}\n")
             print()
             def actualizar_estudiante(estudiantes):
              codigo= input ("ingresa el codigo del estudiante a actualizar: ")
             for est in estudiantes: 
                 if est ["codigo"] == codigo: 
                     est ["nombre"]= input(f" nuevo nombre(actual:{est['nombre']}): ") or est[nombre]
                     est ["apellido"]= input(f" nuevo apellido(actual:{est['apellido']}): ") or est[apellido]
                     est ["carrera"]= input(f" nueva carrera (actual:{est['carrera']}): ") or est[carrera]
                     guardar_estudiantes (estudiantes)
                     print("estudiante actualizado. \n")
                     return 
                 print ("no se encontro estudiante con ese codigo")
                 def eliminar_estudiante(estudiantes):
                     codigo=input ("ingressa el codigo del estudiante a eliminar: ") 
                     for est in estudiantes: 
                         if est ["codigo"] ==codigo: 
                             estudiantes.remove(est)
                             guardar_estudiantes (estudiantes)
                             print ("estudiante eliminado")
                             return 
                         print("no se encontro un estudiante con ese codigo")
                         #funcion principal 
                         def menu(): 
                             estudiantes= cargar_estudiantes()
                             while True: 
                                 print("==== MENU CRUD ESTUDIANTES ====")
                                 print("1. Agregar estudiante")
                                 print("2. Mostrar estudiantes")
                                 print("3. Actualizar estudiante")
                                 print("4. Eliminar estudiante")
                                 print("5. Salir")
                                 opcion = input("Selecciona una opción (1-5): ")
                                 if opcion == "1":
                                  crear_estudiante(estudiantes)
                                 elif opcion == "2":
                                  mostrar_estudiantes(estudiantes)
                                 elif opcion == "3":
                                  actualizar_estudiante(estudiantes)
                                 elif opcion == "4":
                                  eliminar_estudiante(estudiantes)
                                 elif opcion == "5":
                                  print("Saliendo del programa.")
                                 break
                             else:
                               print("Opción no válida.\n")

# Instrucción para ejecutar el menú 
Menu()
                                 