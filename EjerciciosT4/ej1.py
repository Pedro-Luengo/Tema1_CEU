import heapq

# Clase para representar nodos del árbol de Huffman
class Node:
    def _init_(self, value, frequency, left=None, right=None):
        self.value = value
        self.frequency = frequency
        self.left = left
        self.right = right

    def _lt_(self, other):
        # Ordenar primero por frecuencia, luego por orden alfabético para nodos con igual frecuencia
        if self.frequency == other.frequency:
            return self.value < other.value
        return self.frequency < other.frequency

# Clase para representar el árbol de Huffman y sus operaciones
class HuffmanTree:
    def _init_(self, frequencies):
        # Construir árbol de Huffman
        self.root = self.build_huffman_tree(frequencies)
        # Obtener tabla de codificación de Huffman
        self.codes = {}
        self.get_huffman_codes(self.root, "", self.codes)

    # Método para construir el árbol de Huffman a partir de una tabla de frecuencias de caracteres
    # Método para construir el árbol de Huffman a partir de una tabla de frecuencias de caracteres
def build_huffman_tree(self, frequencies):
    # Crear lista de nodos de hojas con sus frecuencias y valores de carácter
    nodes = [Node(value, frequency) for value, frequency in frequencies.items()]
    # Ordenar lista de nodos de hojas de menor a mayor frecuencia
    heapq.heapify(nodes)
    # Mientras queden más de un nodo en la lista:
    while len(nodes) > 1:
        # Tomar los dos nodos con menor frecuencia de la lista
        left, right = heapq.heappop(nodes), heapq.heappop(nodes)
        # Crear un nuevo nodo interno con la suma de las frecuencias de los nodos tomados como hijos izquierdo y derecho, respectivamente
        node = Node(None, left.frequency + right.frequency, left, right)
        # Agregar el nuevo nodo interno a la lista y ordenarla de nuevo
        heapq.heappush(nodes, node)
    # El árbol completo queda formado por el único nodo restante en la lista
    return nodes[0]
# Método para obtener la tabla de codificación de Huffman a partir del árbol de Huffman
def get_huffman_codes(self, node, code, codes):
    if node is None:
        return
    if node.value is not None:
        # Si se llegó a una hoja del árbol, guardar código en la tabla de códigos
        codes[node.value] = code
        return
    # Recorrer subárbol izquierdo con código agregando un cero
    self.get_huffman_codes(node.left, code + "0", codes)
    # Recorrer subárbol derecho con código agregando un uno
    self.get_huffman_codes(node.right, code + "1", codes)
# Método para codificar un mensaje utilizando la tabla de codificación de Huffman
def encode(self, message):
    encoded_message = ""
    # Recorrer cada carácter del mensaje y codificarlo utilizando la tabla de códigos
    for character in message:
        encoded_message += self.codes[character]
    return encoded_message

# Método para descomprimir un mensaje codificado utilizando el árbol de Huffman
def decode(self, encoded_message):
    decoded_message = ""
    # Inicializar nodo actual con la raíz del árbol
    current_node = self.root
    # Recorrer el mensaje codificado bit a bit
    for bit in encoded_message:
        # Si se llegó a una hoja del árbol, se encontró el carácter correspondiente
        if current_node.value is not None:
            decoded_message += current_node.value
            # Reiniciar el nodo actual con la raíz del árbol para seguir buscando el próximo carácter
            current_node = self.root
        # Si se leyó un cero, continuar recorriendo el árbol hacia la izquierda
        if bit == "0":
            current_node = current_node.left
        # Si se leyó un uno, continuar recorriendo el árbol hacia la derecha
        elif bit == "1":
            current_node = current_node.right
    # Añadir el último carácter encontrado al final del mensaje descomprimido
    decoded_message += current_node.value
    return decoded_message
# Mensaje original
message = "Hola, ¿cómo estás?"
# Calcular frecuencias de cada carácter en el mensaje
frequencies = {
    "A": 0.099,
    "B": 0.018,
    "C": 0.036,
    "D": 0.027,
    "E": 0.0125,
    "G": 0.027,
    "I": 0.054,
    "L": 0.054,
    "M": 0.027,
    "N": 0.054,
    "O": 0.063,
    "P": 0.036,
    "Q": 0.009,
    "R": 0.089,
    "S": 0.036,
    "T": 0.027,
    "U": 0.036,
    "V": 0.018,
    " ": 0.152,  # Espacio en blanco
    ",": 0.018,  # Coma
}
for character in message:
    if character in frequencies:
        frequencies[character] += 1
    else:
        frequencies[character] = 1

# Crear árbol de Huffman y obtener tabla de codificación de Huffman
tree = build_huffman_tree(frequencies)

# Codificar mensaje utilizando
# Crear árbol de Huffman y obtener tabla de codificación de Huffman
tree = HuffmanTree(frequencies)

# Codificar mensaje utilizando tabla de codificación de Huffman
encoded_message = tree.encode(message)
print("Mensaje codificado:", encoded_message)

# Descomprimir mensaje codificado utilizando árbol de Huffman
decoded_message = tree.decode(encoded_message)
print("Mensaje descomprimido:", decoded_message)