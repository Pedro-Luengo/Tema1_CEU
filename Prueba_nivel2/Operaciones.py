def suma(a, b):
    try:
        return a + b
    except TypeError:
        print("TypeError: Tipo de dato no válido")

def resta(a, b):
    try:
        return a - b
    except TypeError:
        print("TypeError: Tipo de dato no válido")

def producto(a, b):
    try:
        return a * b
    except TypeError:
        print("TypeError: Tipo de dato no válido")

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("ZeroDivisionError: No es posible dividir entre cero")
    except TypeError:
        print("TypeError: Tipo de dato no válido")