import doctest
class Figura():
    def __init__(self, color, area):
        self.color = color
        self.area = area

    def __str__(self):
        return "Color: {}. ".format(self.color)

    def __gt__(self, other):
      return self.area > other.area

    def __lt__(self, other):
      return self.area < other.area

    def __eq__(self, other):
      return self.area == other.area

class Triangulo(Figura):
    def __init__(self, color, area, base, altura):
        Figura.__init__(self, color, area)
        self.base = base
        self.altura = altura

    def __str__(self):
        return Figura.__str__(self) + "Triangulo de base: {}, altura: {} ".format(self.base, self.altura)

class Circulo(Figura):
    def __init__(self, color, area, radio):
        Figura.__init__(self, color, area)
        self.radio = radio

    def __str__(self):
        return Figura.__str__(self) + "Circulo de radio: {}".format(self.radio)

class Cuadrado(Figura):
    def __init__(self, color, area, lado):
        Figura.__init__(self, color, area)
        self.lado = lado

    def __str__(self):
        return Figura.__str__(self) + "Cuadrado de lado: {} ".format(self.lado)

figuras = [Triangulo("azul", 7.5, 5, 3), Circulo("gris", 78.54, 5), Cuadrado("amarillo", 49, 7)]
def catalogar(figuras):
    for figura in figuras:
        if isinstance(figura, Triangulo):
            print("Triangulo")
        elif isinstance(figura, Circulo):
            print("Circulo")
        elif isinstance(figura, Cuadrado):
            print("Cuadrado")
        print(figura)

def mostrar_areas(figuras):
    for figura in figuras:
        print("La figura {} tiene un area de {} m2".format(figura, figura.area))

def comparar_areas(figura1, figura2):
  area1 = figura1.area
  area2 = figura2.area

  if area1 == area2:
    print("Las figuras {} y {} tienen el mismo área: {} m2".format(figura1, figura2, area1))
  elif area1 > area2:
    print("La figura {} tiene un área mayor que la {}--> {} > {} m2".format(figura1, figura2, area1, area2))
  else:
    print("La figura {} tiene un área menor que la {}--> {} < {} m2".format(figura1, figura2, area1, area2))

def comparar_areas_v2(figura1, figura2):
  if figura1 > figura2:
    print("La figura {} tiene un área mayor que la {}".format(figura1, figura2))
  elif figura1 < figura2:
    print("La figura {} tiene un área menor que la {}".format(figura1, figura2))
  else:
    print("Las figuras {} y {} tienen el mismo área".format(figura1, figura2))

def guardar_figuras(figuras, nombre_fichero):
  with open(nombre_fichero, 'w') as f:
    for figura in figuras:
      f.write(str(figura) + '\n')
  with open(nombre_fichero, 'r') as f:
    contenido = f.read()
  print(contenido)

def cargar_figuras(nombre_fichero):
  figurastxt = []
  with open(nombre_fichero, 'r') as f:
    líneas = f.readlines()
    for línea in líneas:
      figurastxt.append(línea)
  return figurastxt

if __name__ == "__main__":
    doctest.testmod()

    print(catalogar(figuras))
    print(mostrar_areas(figuras))
    print(comparar_areas(figuras[0], figuras[1]))
    print(comparar_areas_v2(figuras[0], figuras[1]))
    print(guardar_figuras(figuras, 'figuras.txt'))
    print(cargar_figuras('figuras.txt'))
    