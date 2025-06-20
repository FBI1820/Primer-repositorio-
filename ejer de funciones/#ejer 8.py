#ejer 8
def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error:No puede dividir entre cero."
x = int(input("Numerador: "))
y = int(input("Denominador: "))
print("respuesta:", division(x, y))
