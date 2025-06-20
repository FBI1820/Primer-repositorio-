def contar(articulo, palabra_buscada):
    try:
        with open(articulo, "r", encoding="utf-8") as archivo:
            contenido = archivo.readline().lower()  
            palabra_buscada = palabra_buscada.lower() 
            palabras = contenido.split() 
            contador = palabras.count(palabra_buscada) 
            
            print(f"La palabra '{palabra_buscada}' aparece {contador} veces en el archivo.")
    except FileNotFoundError:
        print(f"El archivo '{articulo}' no fue encontrado.")
   
palabra_usuario = input("Ingrese la palabra que desea buscar: ")
contar("articulo.txt", palabra_usuario)
