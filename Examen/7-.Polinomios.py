class Nodo(object):
    """Clase nodo simplemente enlazado"""

    info, sig = None, None

class datoPolinomio(Nodo):
    """Clase dato polinomio"""

    def _init_(self, valor, termino):
        """Crea un dato del polinomio con el valor (x^n) y el termino (m)"""
        self.valor = valor
        self.termino = termino
    

class polinomio(datoPolinomio):
    """Clase polinomio"""

    def _init_(self, valor, termino, termino_mayor, grado):
        """Crea un polinomio del grado cero"""
        super()._init_(valor, termino)
        self.termino_mayor = termino_mayor
        self.grado = grado

def agregar_termino(Polinomio, valor, termino):
    """Agregar un termino y un valor al polinomio"""
    aux = Nodo()
    dato = datoPolinomio(valor, termino)
    aux.info = dato
    if(valor > polinomio.termino):
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
    while(aux is not None and aux.info.termino != termino):
        aux = aux.sig
    aux.info.valor = valor

def obtener_valor(polinomio, termino):
    """Devuelve el valor de un termino del polinomio"""
    aux = polinomio.termino_mayor
    while(aux is not None and aux.info.termino > termino):
        aux = aux.sig
    if(aux is not None and aux.info.termino == termino):
        return aux.info.valor
    else:
        return 0

def mostrar(polinomio):
    """Muestra el polinomio"""
    aux = polinomio.termino_mayor
    pol = ""
    if (aux is not None):
        while(aux is not None):
            signo = ""
            if(aux.info.valor>=0):
                signo += "+"
            pol += signo + str(aux.info.valor) + "x^" + str(aux.info.termino)
            aux = aux.sig
    return pol

