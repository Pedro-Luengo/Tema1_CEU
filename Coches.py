class vehiculo:

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"color {self.color}, {self.ruedas} ruedas. "

class coche(vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f"{self.velocidad} km/h, {self.cilindrada} cc"
    
class camioneta(coche):

    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + f"{self.carga} kg"

class bicicleta (vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f"{self.tipo}"

class motocicleta(bicicleta):

    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f"{self.velocidad} km/h, {self.cilindrada} cc"

def catalogar(vehiculos):
    for i in vehiculos:
        print(type(i).__name__, i)

def catalogar(vehiculos, ruedas = None):

    if ruedas != None:
        contador = 0
        for i in vehiculos:
            if i.ruedas == ruedas:
                contador += 1
        print(f"\nSe han encontrado {contador} vehiculor con {ruedas} ruedas. ")
    
    for i in vehiculos:
        if ruedas==None:
            print(type(i).__name__, i)
        else:
            if i.ruedas == ruedas:
                print(type(i).__name__, i)


lista = [
    coche("", , , ),
    camioneta(" ",,,,),
    bicicleta("",,""),
    motocicleta("",,"",,)
]

catalogar(lista)
catalogar(lista, 0)
catalogar(lista, 2)
catalogar(lista, 4)


    