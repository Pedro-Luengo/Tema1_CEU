def crear_tabla(tamaño):
    """Crea una tabla hash vacia"""
    tabla = [None] * tamaño
    return tabla

def cantidad_elementos(tabla):
    """Devuelve la cantidad de elementos en la tabla"""
    return len(tabla) - tabla.count(None)

def cantidad_elementos(tabla):
    """Devuelve la cantidad de elementos en la tabla"""
    return sum(crear_tabla.tamaño(lista) for lista in tabla if lista is not None)

def funcion_hash(dato, tamaño_tabla):
    """Determina la posicion del dato en la tabla"""
    # hash por division para este caso
    return len(str(dato).strip()) % tamaño_tabla

def agregar(tabla, dato):
    """Agrega un elemento a la tabla encadenada"""
    
