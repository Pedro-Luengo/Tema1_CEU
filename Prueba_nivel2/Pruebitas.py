from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.vertices = {}
 
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
 
    def add_edge(self, vertex1, vertex2, weight):
        self.vertices[vertex1].add((vertex2, weight))
        self.vertices[vertex2].add((vertex1, weight))
 
    def get_edges(self, vertex):
        return self.vertices[vertex]


def prim(graph, start):
    # Inicializamos el árbol de expansión y la cola de prioridad
    tree = set()
    queue = PriorityQueue()
 
    # Agregamos el vértice de partida al árbol y añadimos sus aristas a la cola de prioridad
    tree.add(start)
    for edge, weight in graph.get_edges(start):
        queue.put((weight, edge))
 
    # Mientras haya vértices en la cola de prioridad
    while not queue.empty():
        # Obtenemos la arista con mayor peso
        weight, vertex = queue.get()
 
        # Si el vértice no ha sido agregado al árbol de expansión, lo agregamos y añadimos sus aristas a la cola
        if vertex not in tree:
            tree.add(vertex)
            for edge, weight in graph.get_edges(vertex):
                if edge not in tree:
                    queue.put((weight, edge))
 
    return tree
    
graph = {
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
    grafo = Graph()

    # Agregar vértices
    for vertex in graph:
        grafo.add_vertex(vertex)

    # Agregar aristas
    for vertex, edges in graph.items():
        for edge, weight in edges.items():
            grafo.add_edge(vertex, edge, weight)

    # Obtener el árbol de expansión máximo
    print(prim(grafo, 'IronMan'))