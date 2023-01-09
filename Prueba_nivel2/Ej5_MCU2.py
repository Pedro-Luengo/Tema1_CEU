from queue import PriorityQueue

class Grafo:
    def __init__(self):
        self.vertices = {}
 
    def añadir_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = set()
 
    def añadir_aristas(self, vertice1, vertice2, peso):
        self.vertices[vertice1].add((vertice2, peso))
        self.vertices[vertice2].add((vertice1, peso))
 
    def obtener_aristas(self, vertice):
        return self.vertices[vertice]


def prim(grafo, inicio):
    # Inicializamos el árbol de expansión y la cola de prioridad
    tree = set()
    cola = PriorityQueue()
 
    # Agregamos el vértice de partida al árbol y añadimos sus aristas a la cola de prioridad
    tree.add(inicio)
    for arista, peso in grafo.obtener_aristas(inicio):
        cola.put((peso, arista))
 
    # Mientras haya vértices en la cola de prioridad
    while not cola.empty():
        # Obtenemos la arista con mayor peso
        peso, vertice = cola.get()
 
        # Si el vértice no ha sido agregado al árbol de expansión, lo agregamos y añadimos sus aristas a la cola
        if vertice not in tree:
            tree.add(vertice)
            for arista, peso in grafo.obtener_aristas(vertice):
                if arista not in tree:
                    cola.put((peso, arista))
 
    return tree

def obtener_max_episodios(grafo):
    max_episodios = 0
    max_pairs = []
 
    # Buscamos la arista con mayor peso
    for vertice, aristas in grafo.items():
        for arista, peso in aristas.items():
            if peso > max_episodios:
                max_episodios = peso
                max_pares = [(vertice, arista)]
            elif peso == max_episodios:
                max_pairs.append((vertice, arista))
 
    # Buscamos todas las aristas con peso máximo
    for vertice, aristas in grafo.items():
        for arista, peso in aristas.items():
            if peso == max_episodios and (vertice, arista) not in max_pares:
                max_pares.append((vertice, arista))
 
    return max_episodios, max_pares

def obtener_personajes(grafo, episodios):
    personajes = set()
 
    # Recorremos todas las aristas del grafo
    for vertice, aristas in grafo.items():
        for arista, peso in aristas.items():
            # Si el peso de la arista es igual al número de episodios deseado, agregamos los vértices a la lista
            if peso == episodios:
                personajes.add(vertice)
                personajes.add(arista)
 
    return personajes
 

grafo1 = {
'IronMan': {'Hulk': 6, 'Khan': 0, 'Thor': 1, 'CapitanAmerica': 8, 'Antman': 7, 'NickFury': 3, 'WinterSoldier': 2},
'Hulk': {'IronMan': 6, 'Khan': 0, 'Thor': 6, 'CapitanAmerica': 1, 'Antman': 8, 'NickFury': 9, 'WinterSoldier': 1},
'Khan': {'IronMan': 0, 'Hulk': 0, 'Thor': 1, 'CapitanAmerica': 2, 'Antman': 1, 'NickFury': 5, 'WinterSoldier': 0},
'Thor': {'IronMan': 1, 'Hulk': 6, 'Khan': 1, 'CapitanAmerica': 1, 'Antman': 5, 'NickFury': 9, 'WinterSoldier': 3},
'CapitanAmerica': {'IronMan': 8, 'Hulk': 1, 'Khan': 2, 'Thor': 1, 'Antman': 2, 'NickFury': 4, 'WinterSoldier': 5},
'Antman': {'IronMan': 7, 'Hulk': 8, 'Khan': 1, 'Thor': 5, 'CapitanAmerica': 2, 'NickFury': 1, 'WinterSoldier': 6},
'NickFury': {'IronMan': 3, 'Hulk': 9, 'Khan': 5, 'Thor': 9, 'CapitanAmerica': 4, 'Antman': 1, 'WinterSoldier': 1},
'WinterSoldier': {'IronMan': 2, 'Hulk': 1, 'Khan': 0, 'Thor': 3, 'CapitanAmerica': 5, 'Antman': 6, 'NickFury': 1}
}
if __name__ == '__main__':
    #Creación del grafo no dirigido
    grafo = Grafo()

    # Agregar vértices
    for vertice in grafo1:
        grafo.añadir_vertice(vertice)

    # Agregar aristas
    for vertice, aristas in grafo1.items():
        for arista, peso in aristas.items():
            grafo.añadir_aristas(vertice, arista, peso)

    # Obtener el árbol de expansión máximo
    print(prim(grafo, 'IronMan'))

    # Obtener el número maximo de episodios y los pares de episodios que comparten dichos personajes
    print(obtener_max_episodios(grafo1))

    # Obtener los personajes que aparecen en 9 episodios
    print(obtener_personajes(grafo1, 9))