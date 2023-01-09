import random

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

class Baraja:
    def __init__(self):
        self.cartas = []

    def generar_baraja(self):
        for valor in range(1, 13):
            for palo in ['espada', 'basto', 'copa', 'oro']:
                self.cartas.append(Carta(valor, palo))
        random.shuffle(self.cartas)
        return self.cartas

    def separar_por_palo(self):
        espadas = []
        bastos = []
        copas = []
        oros = []
        for carta in self.cartas:
            if carta.palo == 'espada':
                espadas.append(carta)
            elif carta.palo == 'basto':
                bastos.append(carta)
            elif carta.palo == 'copa':
                copas.append(carta)
            elif carta.palo == 'oro':
                oros.append(carta)
        return espadas, bastos, copas, oros

    def ordenar_por_valor(self, espadas, bastos, copas, oros):
        espadas.sort(key=lambda x: x.valor)
        bastos.sort(key=lambda x: x.valor)
        copas.sort(key=lambda x: x.valor)
        oros.sort(key=lambda x: x.valor)
        return espadas, bastos, copas, oros
    
    def listas_copias(self, espadas, bastos, copas, oros):
        espadas_copy = []
        bastos_copy = []
        copas_copy = []
        oros_copy = []
        for carta in espadas:
            espadas_copy.append(f"{carta.valor} de {carta.palo}, ")
        for carta in bastos:
            bastos_copy.append(f"{carta.valor} de {carta.palo}, ")
        for carta in copas:
            copas_copy.append(f"{carta.valor} de {carta.palo}, ")
        for carta in oros: 
            oros_copy.append(f"{carta.valor} de {carta.palo}, ")
        return espadas_copy, bastos_copy, copas_copy, oros_copy
# Creamos una instancia de la clase Deck
baraja = Baraja()

# Generamos el mazo de forma aleatoria
baraja.generar_baraja()

# Separamos las cartas por palo
espadas, bastos, copas, oros = baraja.separar_por_palo()
print(espadas, bastos, copas, oros, sep="\n")

# Ordenamos las cartas de espadas
baraja.ordenar_por_valor(espadas, bastos, copas, oros)
print(baraja.listas_copias(espadas, bastos, copas, oros) , sep="\n")