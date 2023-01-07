class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = {}

class Grafo:
    def __init__(self):
        self.personajes = {}

    def agregar_personaje(self, personaje):
        self.personajes[personaje.nombre] = personaje

    def agregar_arista(self, personaje1, personaje2, episodios):
        self.personajes[personaje1].vecinos[personaje2] = episodios
        self.personajes[personaje2].vecinos[personaje1] = episodios

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

# Creamos una instancia de la clase Grafo
g = Grafo()

g.agregar_personaje(Personaje("IronMan"))
g.agregar_personaje(Personaje("Hulk"))
g.agregar_personaje(Personaje("Khan"))
g.agregar_personaje(Personaje("Thor"))
g.agregar_personaje(Personaje("CapitanAmerica"))
g.agregar_personaje(Personaje("Antman"))
g.agregar_personaje(Personaje("NickFury"))
g.agregar_personaje(Personaje("WinterSoldier"))

# Recorremos el diccionario de diccionarios
for nombre, vecinos in graph.items():
    # Recorremos el diccionario de vecinos
    for nombre_vecino, episodios in vecinos.items():
        # Agregamos una arista entre el personaje y su vecino
        g.agregar_arista(nombre, nombre_vecino, episodios)