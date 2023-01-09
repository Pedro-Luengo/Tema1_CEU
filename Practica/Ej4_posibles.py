from collections import defaultdict
from heapq import heapify, heappop, heappush

# Clase que representa un nodo en el árbol de Huffman
class HuffmanNode:
    def __init__(self, peso, ch=None, left=None, right=None):
        self.peso = peso
        self.ch = ch
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.peso < other.peso

# Función que construye el árbol de Huffman a partir de una tabla de frecuencias
def build_huffman_tree(frequencias):
    # Crear la lista de nodos de hoja a partir de la tabla de frecuencias
    nodo_hoja = [HuffmanNode(f, ch) for ch, f in frequencias.items()]

    # Ordenar la lista de nodos de hoja en orden creciente de peso
    heapify(nodo_hoja)

    # Mientras haya más de un nodo en la lista, tomar los dos con menor peso
    # y crear un nuevo nodo interno como padre de ambos, con el peso igual a
    # la suma de los pesos de los nodos hijo
    while len(nodo_hoja) > 1:
        left = heappop(nodo_hoja)
        right = heappop(nodo_hoja)
        nodo_interno = HuffmanNode(left.peso + right.peso, left=left, right=right)
        heappush(nodo_hoja, nodo_interno)

# El último nodo en la lista es la raíz del árbol de Huffman
    return nodo_hoja[0]

def generar_codigo_huffman(huffman_tree, codes, prefix=""):
    if huffman_tree.ch is not None:
        # Es un nodo de hoja, asignar el código al diccionario de códigos
        codes[huffman_tree.ch] = prefix
    else:
        # Es un nodo interno, recorrer sus hijos
        generar_codigo_huffman(huffman_tree.left, codes, prefix + "0")
        generar_codigo_huffman(huffman_tree.right, codes, prefix + "1")

def comprimir_mensaje(mensaje, frequencias):
    huffman_tree = build_huffman_tree(frequencias)
    codigos = defaultdict(str)
    generar_codigo_huffman(huffman_tree, codigos)

    mensaje_comprimido = ""
    for ch in mensaje:
        mensaje_comprimido += codigos[ch]

    return mensaje_comprimido
    
def descomprimir_mensaje(mensaje_comprimido, frequencias):
    huffman_tree = build_huffman_tree(frequencias)
    mensaje = ""
    nodo_actual = huffman_tree

    for bit in mensaje_comprimido:
        if bit == "0":
            nodo_actual = nodo_actual.left
        else:
            nodo_actual = nodo_actual.right

        if nodo_actual.ch is not None:
            mensaje += nodo_actual.ch
            nodo_actual = huffman_tree

    return mensaje

# Ejemplo de uso

frequencias = {
    "A": 0.2,
    "B": 0.21,
    "1": 0.13,
    "5": 0.17,
    "3": 0.05,
    "J": 0.15,
    "Z": 0.09,
}

if __name__ == "__main__":

    mensaje = "JBA51AB3J5Z5A5J5J5A5A5"
    print(comprimir_mensaje(mensaje, frequencias)) # Imprime algo como "0101010101"
    print(descomprimir_mensaje(comprimir_mensaje(mensaje, frequencias), frequencias))# Imprime "A5J5J5A5A5"
