## Ejercicio 7
'''
Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. La función debe añadir el elemento al final de la lista con la condición de no 
repetir ningún elemento. Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar 
este mensaje en su lugar:

Error: Imposible añadir elementos duplicados => [elemento].
Cuando tengas la función intenta añadir los siguiente valores a la lista 10, -2, "Hola" y luego muestra su contenido.

Sugerencia

Puedes utilizar la sintaxis "elemento in lista"

elementos = [1, 5, -2]
'''
def agregar_una_vez():
    lista = []
    for i in range(10):
        valor = input("Escriba los valores que tendra la lista: ")
        lista.append(valor)
    elemento = input("Escriba el elemento que quiere añadir a la lista: ")
    if elemento in lista:
        print("Error: Imposible añadir elementos duplicados => [" + elemento + "].")
    else:
        lista.append(elemento)
    print(lista)
agregar_una_vez()