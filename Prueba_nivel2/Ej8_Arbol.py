from random import randint

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree(Node):
    def __init__(self):
        self.root = None

    def add_node(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while current_node is not None:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right

    def preorder(self, node):
        if node is not None:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

    def levelorder(self, node):
        if node is not None:
            queue = [node]
            while len(queue) > 0:
                node = queue.pop(0)
                print(node.value, end=" ")
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

    def search(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self.search(node.left, value)
        else:
            return self.search(node.right, value)

    

    def delete_node(self, node, value):
        if node is None:  # el nodo no existe en el árbol
            return None

        if value < node.value:  # busca el nodo en el subárbol izquierdo
            node.left = self.delete_node(node.left, value)
        elif value > node.value:  # busca el nodo en el subárbol derecho
            node.right = self.delete_node(node.right, value)
        else:  # encontró el nodo a eliminar
            if not node.left and not node.right:  # es una hoja
                node = None  # elimina el nodo
            elif not node.left or not node.right:  # tiene un solo hijo
                node = node.left or node.right  # enlaza al hijo con el padre
                return node
            else: # tiene dos hijos
                predecessor = self.get_predecessor(node)
                node.value = predecessor.value
                node.left = self.delete_node(node.left, predecessor.value)
                return node

    def delete(self, value):
            self.root = self.delete_node(self.root, value)
    
    def delete_three(self, value1, value2, value3):
        self.delete(value1)
        self.delete(value2)
        self.delete(value3)

    def get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
        

    def get_left_height(self, node):
        if node is None:
            return 0
        left_height = self.get_left_height(node.left)
        if left_height == 0:
            return 1
        return 1 + left_height
    
    def get_right_height(self, node):
        if node is None:
            return 0
        right_height = self.get_right_height(node.right)
        if right_height == 0:
            return 1
        return 1 + right_height

    def count_occurrences(self, node, value):
        if node is None:
            return 0
        count = 0
        if node.value == value:
            count += 1
        count += self.count_occurrences(node.left, value)
        count += self.count_occurrences(node.right, value)
        return count

    def count_odd_even(self, node):
        if node is None:
            return (0, 0)

        (odd_left, even_left) = self.count_odd_even(node.left)
        (odd_right, even_right) = self.count_odd_even(node.right)

        if node.value % 2 == 0:
            return (odd_left + odd_right, even_left + even_right + 1)
        else:
            return (odd_left + odd_right + 1, even_left + even_right)

if __name__ == "__main__":

    arbol = Tree()
    #Agrego nodos
    for i in range(1000):
        arbol.add_node(randint(1,1000))
    
    #Imprimo la altura de cada lado del arbol
    
    #Hago los barridos  
    #arbol.preorder(arbol.root)
    #arbol.inorder(arbol.root)
    #arbol.postorder(arbol.root)
    #arbol.levelorder(arbol.root)
    #arbol.search(arbol.root, 500)
    
    #Busco tres valores
    print(arbol.search(arbol.root, 500))
    print(arbol.search(arbol.root, 600))
    print(arbol.search(arbol.root, 700))
    

    

    print(arbol.get_left_height(arbol.root))
    print(arbol.get_right_height(arbol.root))

    

    #Cuento la cantidad de ocurrencias de un valor
    print(arbol.count_occurrences(arbol.root, 500))

    #Cuento la cantidad de valores pares e impares
    print(arbol.count_odd_even(arbol.root))

    #Elimino nodos
    arbol.delete_three(500, 600, 700)
