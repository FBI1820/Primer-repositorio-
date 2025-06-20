#ejer 7
def calcular_total(precio, cantidad):
    subtotal = precio * cantidad
    iva = subtotal * 0.15 
    return subtotal + iva

precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
total = calcular_total(precio, cantidad)
print("Total a pagar:", total)
