import doctest
from heapq import heappush, heappop

class Vertice:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def __eq__(self, other):
        if isinstance(other, Vertice):
            return self.nombre == other.nombre
        return False

    def __hash__(self):
        return hash(self.nombre)
    
    def __lt__(self, other):
        # Compara los atributos de dos objetos Vertice de la forma que desees
        return self.nombre < other.nombre

class Grafo:
    def __init__(self):
        self.vertices = {}
        self.aristas = []
    
    def agregar_vertice(self, vertice):
        self.vertices[vertice.nombre] = vertice
    
    def agregar_arista(self, vertice1, vertice2):
        if vertice1.tipo == "estación" and vertice2.tipo == "estación":
            # No agregamos la arista porque ambos vértices son estaciones
            return
        if vertice1.tipo == "estacion" and len(grafo.obtener_adyacentes(vertice1)) >= 2 or vertice2.tipo == "estacion" and len(grafo.obtener_adyacentes(vertice2)) >= 2:
            return

        if vertice1.tipo == "desvio" and len(grafo.obtener_adyacentes(vertice1)) >= 4 or vertice2.tipo == "desvio" and len(grafo.obtener_adyacentes(vertice2)) >= 4:
            return    

        self.aristas.append((vertice1, vertice2))

    def obtener_adyacentes(self, vertice):
        adyacentes = []
        for arista in self.aristas:
            vertice1, vertice2 = arista
            peso = 1
            if vertice1 == vertice:
                adyacentes.append((vertice2, peso))
            if vertice2 == vertice:
                adyacentes.append((vertice1, peso))
        return adyacentes

# Creamos el grafo
grafo = Grafo()

# Creamos los vértices
estacion1 = Vertice("King's Cross", "estacion")
estacion2 = Vertice("Liverpool Street Station", "estacion")
estacion3 = Vertice("Victoria Train Station", "estacion")
estacion4 = Vertice("Euston", "estacion")
estacion5 = Vertice("Waterloo", "estacion")
estacion6 = Vertice("St. Pancras", "estacion")
desvio1 = Vertice("1", "desvio")
desvio2 = Vertice("2", "desvio")
desvio3 = Vertice("3", "desvio")
desvio4 = Vertice("4", "desvio")
desvio5 = Vertice("5", "desvio")
desvio6 = Vertice("6", "desvio")
desvio7 = Vertice("7", "desvio")
desvio8 = Vertice("8", "desvio")
desvio9 = Vertice("9", "desvio")
desvio10 = Vertice("10", "desvio")
desvio11 = Vertice("11", "desvio")
desvio12 = Vertice("12", "desvio")

# Agregamos los vértices al grafo
grafo.agregar_vertice(estacion1)
grafo.agregar_vertice(estacion2)
grafo.agregar_vertice(estacion3)
grafo.agregar_vertice(estacion4)
grafo.agregar_vertice(estacion5)
grafo.agregar_vertice(estacion6)
grafo.agregar_vertice(desvio1)
grafo.agregar_vertice(desvio2)
grafo.agregar_vertice(desvio3)
grafo.agregar_vertice(desvio4)
grafo.agregar_vertice(desvio5)
grafo.agregar_vertice(desvio6)
grafo.agregar_vertice(desvio7)
grafo.agregar_vertice(desvio8)
grafo.agregar_vertice(desvio9)
grafo.agregar_vertice(desvio10)
grafo.agregar_vertice(desvio11)
grafo.agregar_vertice(desvio12)

# Conectamos cada estación con un desvío
grafo.agregar_arista(estacion1, desvio1)
grafo.agregar_arista(estacion2, desvio2)
grafo.agregar_arista(estacion3, desvio3)
grafo.agregar_arista(estacion4, desvio4)
grafo.agregar_arista(estacion5, desvio5)
grafo.agregar_arista(estacion6, desvio6)
grafo.agregar_arista(estacion1, desvio7)
grafo.agregar_arista(estacion2, desvio8)
grafo.agregar_arista(estacion3, desvio9)
grafo.agregar_arista(estacion4, desvio10)
grafo.agregar_arista(estacion5, desvio11)
grafo.agregar_arista(estacion6, desvio12)

# Conectamos los desvíos entre sí
grafo.agregar_arista(desvio1, desvio8)
grafo.agregar_arista(desvio1, desvio9)
grafo.agregar_arista(desvio2, desvio7)
grafo.agregar_arista(desvio2, desvio11)
grafo.agregar_arista(desvio3, desvio12)
grafo.agregar_arista(desvio3, desvio7)
grafo.agregar_arista(desvio4, desvio12)
grafo.agregar_arista(desvio4, desvio9)
grafo.agregar_arista(desvio5, desvio10)
grafo.agregar_arista(desvio5, desvio8)
grafo.agregar_arista(desvio6, desvio11)
grafo.agregar_arista(desvio6, desvio10)
grafo.agregar_arista(desvio1, desvio4)
grafo.agregar_arista(desvio7, desvio10)
grafo.agregar_arista(desvio2, desvio5)
grafo.agregar_arista(desvio8, desvio11)
grafo.agregar_arista(desvio3, desvio6)
grafo.agregar_arista(desvio9, desvio12)



def dijkstra(grafo, vertice_inicial, vertice_final):
    # Diccionario que almacena las distancias mínimas desde el vertice_inicial a cada uno de los vértices del grafo 
    distancias = {vertice: float("inf") for vertice in grafo.vertices.values()}
    # Diccionario que almacena el vértice anterior en el camino más corto desde el vertice_inicial a cada uno de los vértices del grafo
    predecesores = {vertice: None for vertice in grafo.vertices.values()}
    # Marca todos los vértices como no visitados
    visitados = {vertice: False for vertice in grafo.vertices.values()}
    # Inicializamos la distancia del vertice_inicial a 0
    distancias[vertice_inicial] = 0
    # Cola de prioridad para seleccionar el vértice con la distancia mínima en cada iteración
    cola = [(0, vertice_inicial)]

    # Mientras la cola no esté vacía...
    while cola:
        # Tomamos el vértice con la distancia mínima de la cola
        distancia, vertice = heappop(cola)
        # Si ya hemos visitado este vértice, continuamos con la siguiente iteración
        if visitados[vertice]:
            continue
        # Marcamos el vértice como visitado
        visitados[vertice] = True
        # Recorremos todos vertices adyacentes al vértice actual
        for adyacente, peso in grafo.obtener_adyacentes(vertice):
        # Si la distancia del vértice actual al vértice adyacente es menor que la distancia actual del vértice adyacente, actualizamos la distancia y el vértice predecesor del vértice adyacente
            if distancias[vertice] + peso < distancias[adyacente]:
                distancias[adyacente] = distancias[vertice] + peso
                predecesores[adyacente] = vertice
                heappush(cola, (distancias[adyacente], adyacente))
        #Una vez que hemos terminado de recorrer todos los vértices, podemos obtener el camino más corto desde el vértice inicial hasta el vértice final recorriendo el diccionario de predecesores desde el vértice final hasta el inicial
        camino = []
        vertice = vertice_final
        while vertice is not None:
            camino.append(vertice)
            vertice = predecesores[vertice]
        # Invertimos el camino para obtener el orden correcto
        camino = camino[::-1]
        # Devolvemos el camino más corto y su distancia
    return f"El camino mas corto es: {[vertice.nombre for vertice in camino]}. A una distancia de:  {distancias[vertice_final]}." 



if __name__ == "__main__":

    # Buscamos el camino más corto entre el vértice A y el vértice D
    print(dijkstra(grafo, estacion2, estacion6))
