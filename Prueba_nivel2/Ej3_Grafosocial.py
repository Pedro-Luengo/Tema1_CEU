class Superhero:
    def __init__(self, name):
        self.name = name
        self.ig_connections = {}
        self.tw_connections = {}

    def add_connection(self, superhero, ig_weight, tw_weight):
        self.ig_connections[superhero] = ig_weight
        superhero.ig_connections[self] = ig_weight
        self.tw_connections[superhero] = tw_weight
        superhero.tw_connections[self] = tw_weight

class Graph:
    def __init__(self):
        self.superheroes = []

    def add_superhero(self, superhero):
        self.superheroes.append(superhero)

    def add_connection(self, superhero1, superhero2, weight):
        superhero1.add_connection(superhero2, weight)
        superhero2.add_connection(superhero1, weight)

    def vertex_degree(self, superhero):
        return len(superhero.connections)

#Creamos los superheroes, que seran los vertices.
Ironman = Superhero("Ironman")
Hulk = Superhero("Hulk")
Khan = Superhero("Khan")
Thor = Superhero("Thor")
CaptainAmerica = Superhero("Captain America")
Antman = Superhero("Antman")
NickFury = Superhero("Nick Fury")
WinterSoldier = Superhero("Winter Soldier")

#Agregamos las conexiones entre superheroes.
Ironman.add_connection(Hulk, 75, 61)
Ironman.add_connection(Khan, 40, 44)
Ironman.add_connection(Thor, 16, 66)
Ironman.add_connection(CaptainAmerica, 80, 56)
Ironman.add_connection(Antman, 20, 74)
Ironman.add_connection(NickFury, 99, 11)
Ironman.add_connection(WinterSoldier, 23, 65)
Hulk.add_connection(Khan, 50, 47)
Hulk.add_connection(Thor, 67, 41)
Hulk.add_connection(CaptainAmerica, 79, 12)
Hulk.add_connection(Antman, 38, 38)
Hulk.add_connection(NickFury, 99, 99)
Hulk.add_connection(WinterSoldier, 41, 41)
Khan.add_connection(Thor, 0.5, 0.5)
Khan.add_connection(CaptainAmerica, 0.5, 0.5)
Khan.add_connection(Antman, 0.5, 0.5)
Khan.add_connection(NickFury, 0.5, 0.5)
Khan.add_connection(WinterSoldier, 0.5, 0.5)
Thor.add_connection(CaptainAmerica, 0.5, 0.5)
Thor.add_connection(Antman, 0.5, 0.5)
Thor.add_connection(NickFury, 0.5, 0.5)
Thor.add_connection(WinterSoldier, 0.5, 0.5)
CaptainAmerica.add_connection(Antman, 0.5, 0.5)
CaptainAmerica.add_connection(NickFury, 0.5, 0.5)
CaptainAmerica.add_connection(WinterSoldier, 0.5, 0.5)
Antman.add_connection(NickFury, 0.5, 0.5)
Antman.add_connection(WinterSoldier, 0.5, 0.5)
NickFury.add_connection(WinterSoldier, 0.5, 0.5)




