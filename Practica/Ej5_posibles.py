class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.longitud = 0

    def append(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.longitud == 0:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.longitud += 1

def obtener_cambio(cantidad, monedas):
    cambio = ListaEnlazada()
    for moneda in reversed(monedas):
        while moneda <= cantidad:
            cambio.append(moneda)
            cantidad -= moneda
    return cambio

if __name__ == '__main__':

    # Prueba con el primer ejemplo
    cantidad = 342
    monedas = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    cambio = obtener_cambio(cantidad, monedas)
    nodo = cambio.cabeza
    print(f"Se necesitan {cambio.longitud} monedas/billetes:")
    while nodo is not None:
        print(nodo.valor)
        nodo = nodo.siguiente

    # Prueba con el segundo ejemplo
    cantidad = 67
    monedas = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    cambio = obtener_cambio(cantidad, monedas)
    nodo = cambio.cabeza
    print(f"Se necesitan {cambio.longitud} monedas/billetes:")
    while nodo is not None:
        print(nodo.valor)
        nodo = nodo.siguiente