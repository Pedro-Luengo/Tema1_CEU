import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Deck:
    def __init__(self):
        self.cards = []

    def generate_deck(self):
        for value in range(1, 13):
            for suit in ['espada', 'basto', 'copa', 'oro']:
                self.cards.append(Card(value, suit))
        random.shuffle(self.cards)
        return self.cards

    def separate_by_suit(self):
        spades = []
        clubs = []
        cups = []
        golds = []
        for card in self.cards:
            if card.suit == 'espada':
                spades.append(card)
            elif card.suit == 'basto':
                clubs.append(card)
            elif card.suit == 'copa':
                cups.append(card)
            elif card.suit == 'oro':
                golds.append(card)
        return spades, clubs, cups, golds

    def sort_by_value(self, spades, clubs, cups, golds):
        spades.sort(key=lambda x: x.value)
        clubs.sort(key=lambda x: x.value)
        cups.sort(key=lambda x: x.value)
        golds.sort(key=lambda x: x.value)
        return spades , clubs, cups, golds
    
    def listas_copias(self, spades, clubs, cups, golds):
        spades_copy = []
        clubs_copy = []
        cups_copy = []
        golds_copy = []
        for carta in spades:
            spades_copy.append(f"{carta.value} de {carta.suit}, ")
        for carta in clubs:
            clubs_copy.append(f"{carta.value} de {carta.suit}, ")
        for carta in cups:
            cups_copy.append(f"{carta.value} de {carta.suit}, ")
        for carta in golds: 
            golds_copy.append(f"{carta.value} de {carta.suit}, ")
        return spades_copy, clubs_copy, cups_copy, golds_copy
# Creamos una instancia de la clase Deck
deck = Deck()

# Generamos el mazo de forma aleatoria
deck.generate_deck()

# Separamos las cartas por palo
spades, clubs, cups, golds = deck.separate_by_suit()
print(spades, clubs, cups, golds, sep="\n")

# Ordenamos las cartas de espadas
deck.sort_by_value(spades, clubs, cups, golds)
print(deck.listas_copias(spades, clubs, cups, golds) , sep="\n")