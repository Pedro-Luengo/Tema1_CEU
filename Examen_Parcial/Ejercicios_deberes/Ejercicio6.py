## Ejercicio 6
'''
Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.

Por ejemplo:

pares, impares = separar([6,5,2,1,7])

print(pares)

print(impares)

[2, 6]

[1, 5, 7]

Sugerencia

Para ordenar una lista automáticamente puedes utilizar el método .sort().
'''
def separar_lista():
    lista = [3,5,6,8,16,20,1,73,4]
    lista_pares = []
    lista_impares = []
    for a in lista:
        if int(a) % 2 == 0:
            lista_pares.append(a)
        elif int(a) % 2 != 0:
            lista_impares.append(a)
    print(sorted(lista_pares))
    print(sorted(lista_impares))
separar_lista()