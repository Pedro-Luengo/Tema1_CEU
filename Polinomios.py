class Nodo(object):
    """Clase nodo simplemente enlazado"""

    info, sig = None, None

class datoPolinomio(object):
    """Clase dato polinomio"""

    def __init__(self, valor, termino):
        """Crea un dato polinomio con el valor y el termino"""
        self.valor = valor
        self.termino = termino
    

class polinomio(object):
    """Clase polinomio"""

    def __init__(self, termino_mayor, grado):
        """Crea un polinomio del grado cero"""
        self.termino_mayor = termino_mayor
        self.grado = grado

def agregar_termino(polinomio, termino, valor):
    """Agregar un termino y un valor al polinomio"""
    aux = Nodo()
    dato = datoPolinomio(valor, termino)
    aux.info = dato
    if(termino > polinomio.grado):
        aux.sig = polinomio.termino_mayor
        polinomio.termino_mayor = aux
        polinomio.grado = termino
    else:
        actual = polinomio.termino_mayor
        while(actual.sig is not None and termino < actual.sig.info.termino):
            actual = actual.sig
        aux.sig = actual.sig
        actual.sig = aux

def modificar_termino(polinomio, termino, valor):
    """Modifica un termino del polinomio"""
    aux = polinomio.termino_mayor
    while(aux is not None )
