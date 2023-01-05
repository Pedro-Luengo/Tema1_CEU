from collections import defaultdict
from heapq import heapify, heappop, heappush

# Clase que representa un nodo en el árbol de Huffman
class HuffmanNode:
    def __init__(self, weight, ch=None, left=None, right=None):
        self.weight = weight
        self.ch = ch
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.weight < other.weight

# Función que construye el árbol de Huffman a partir de una tabla de frecuencias
def build_huffman_tree(frequencies):
    # Crear la lista de nodos de hoja a partir de la tabla de frecuencias
    leaf_nodes = [HuffmanNode(f, ch) for ch, f in frequencies.items()]

    # Ordenar la lista de nodos de hoja en orden creciente de peso
    heapify(leaf_nodes)

    # Mientras haya más de un nodo en la lista, tomar los dos con menor peso
    # y crear un nuevo nodo interno como padre de ambos, con el peso igual a
    # la suma de los pesos de los nodos hijo
    while len(leaf_nodes) > 1:
        left = heappop(leaf_nodes)
        right = heappop(leaf_nodes)
        internal_node = HuffmanNode(left.weight + right.weight, left=left, right=right)
        heappush(leaf_nodes, internal_node)

# El último nodo en la lista es la raíz del árbol de Huffman
    return leaf_nodes[0]

def generate_huffman_codes(huffman_tree, codes, prefix=""):
    if huffman_tree.ch is not None:
        # Es un nodo de hoja, asignar el código al diccionario de códigos
        codes[huffman_tree.ch] = prefix
    else:
        # Es un nodo interno, recorrer sus hijos
        generate_huffman_codes(huffman_tree.left, codes, prefix + "0")
        generate_huffman_codes(huffman_tree.right, codes, prefix + "1")

def compress_message(message, frequencies):
    huffman_tree = build_huffman_tree(frequencies)
    codes = defaultdict(str)
    generate_huffman_codes(huffman_tree, codes)

    compressed_message = ""
    for ch in message:
        compressed_message += codes[ch]

    return compressed_message
    
def decompress_message(compressed_message, frequencies):
    huffman_tree = build_huffman_tree(frequencies)
    message = ""
    current_node = huffman_tree

    for bit in compressed_message:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.ch is not None:
            message += current_node.ch
            current_node = huffman_tree

    return message

# Ejemplo de uso

frequencies = {
    "A": 0.2,
    "B": 0.21,
    "1": 0.13,
    "5": 0.17,
    "3": 0.05,
    "J": 0.15,
    "Z": 0.09,
}

if __name__ == "__main__":

    message = "JBA51AB3J5Z5A5J5J5A5A5"
    print(compress_message(message, frequencies)) # Imprime algo como "0101010101"
    print(decompress_message(compress_message(message, frequencies), frequencies))# Imprime "A5J5J5A5A5"
