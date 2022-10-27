numeros = [18, 50, 210, 80, 145, 333, 70, 30]

def modificar(lista):
    multiplos1 = []
    for n in lista:
        if n % 10 == 0 and  n < 200:
            multiplos1.append(n)
    return multiplos1

multiplos = modificar(numeros)
print(multiplos)

def modificar_2(lista):
    multiplos2 = []
    for n in lista:
        if n > 300:
            break        
        if n % 10 == 0 and  n < 200:
            multiplos2.append(n)
    return multiplos2

multiplos_2 = modificar_2(numeros)
print(multiplos_2)

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


def indice(lista):
    if 145 in lista:
        print(numeros.index(145))
    else:
        print("-1")
    return indice
indice(numeros)