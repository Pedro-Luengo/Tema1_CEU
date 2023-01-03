lista = [2,5,43,7,2,97,49,3,6,13,18,13,15.5]
def modificar(lista):
    #Borramos los elementos duplicados
    lista_sin_duplicados = list(set(lista))
    #Ordenamos la lista de mayor a menor
    lista_ordenada = sorted(lista_sin_duplicados, reverse=True)
    #Eliminamos los números impares
    lista_sin_impares = [num for num in lista_ordenada if num % 2 == 0]
    #Realizamos la suma de los números restantes
    suma = sum(lista_sin_impares)
    #Añadimos la suma como primer elemento de la lista
    lista_modificada = [suma] + lista_sin_impares
    return lista_modificada

nueva_lista = modificar(lista)
print( nueva_lista[0] == sum(nueva_lista[1:]) )