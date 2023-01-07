import math
import random


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

def leer_numero(ini, fin, mensaje):
    while True:
        try:
            num = int(input(mensaje))
            if num < ini or num > fin:
                raise ValueError
            return num
        except ValueError:
            print(f"Error: El número debe estar entre {ini} y {fin} (inclusive).")
        except:
            print("Error: Tipo de dato no válido.")



def generador():
    numeros = leer_numero(1, 20, "¿Cuántos números quieres generar? [1-20]: ")
    modo = leer_numero(1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")

    numeros_redondeados = []
    for i in range(numeros):
        num = random.uniform(0, 100)
        if modo == 1:
            num_redondeado = math.ceil(num)
        elif modo == 2:
            num_redondeado = math.floor(num)
        else:
            num_redondeado = round(num)
        print(f"{num} => {num_redondeado}")
        numeros_redondeados.append(num_redondeado)
    return numeros_redondeados