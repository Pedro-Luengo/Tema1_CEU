## Ejercicio 3
'''
Dadas dos listas, debes generar una tercera con todos los elementos que se repitan
en ellas, pero no debe repetirse ningún elemento en la nueva lista:
'''

def elementos_repetidos():
    lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']

    lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

    lista_3 = []

    for letra in lista_1:
        if letra in lista_2:
            if letra not in lista_3:
                lista_3 += letra
            else:
                pass
    print(lista_3)
elementos_repetidos()
