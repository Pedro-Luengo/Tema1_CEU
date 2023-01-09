numeros = [18, 50, 210, 80, 145, 333, 70, 30]

#Apartado 1
#Creo una funcion que me creee una lista aparta con multiplos de 10 y valores menores a 200.
def imprimir(lista):
    multiplos1 = []
    for n in lista:
        if n % 10 == 0 and  n < 200:
            multiplos1.append(n)
    return multiplos1

multiplos = imprimir(numeros)
print(multiplos)

#Apartado 2
#Hago lo mismo que en el apartado anterior pero si el valor es >300 salgo del bucle.
def imprimir_2(lista):
    multiplos2 = []
    for n in lista:
        if n > 300:
            break        
        if n % 10 == 0 and  n < 200:
            multiplos2.append(n)
    return multiplos2

multiplos_2 = imprimir_2(numeros)
print(multiplos_2)

#Apartado 3
#Utilizo la funcion merge_sort() para ordenar la lista inicial de menor a mayor.
def merge_sort(coleccion: list) -> list:
    def merge(izquierda: list, derecha: list) -> list:

            def _merge():
                while izquierda and derecha:
                    yield (izquierda if izquierda[0] <= derecha[0] else derecha).pop(0)
                yield from izquierda
                yield from derecha

            return list(_merge())

    if len(coleccion) <= 1:
            return coleccion
    mid = len(coleccion) // 2
    return merge(merge_sort(coleccion[:mid]), merge_sort(coleccion[mid:]))

print(merge_sort(numeros), sep=",")

#Apartado 4
#Finalmente hago una funcion indice para que me de el valor del indice en las dos situaciones.
def indice(lista):
    if 145 in lista:
        print(numeros.index(145))
    else:
        print("-1")
    return indice
indice(numeros)