
class Node:
  def __init__(self, valor):
    self.valor = valor
    self.siguiente = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def append(self, valor):
    nuevo_nodo = Node(valor)
    if self.head is None:
      self.head = nuevo_nodo
      return
    ultimo_nodo = self.head
    while ultimo_nodo.siguiente:
      ultimo_nodo = ultimo_nodo.siguiente
    ultimo_nodo.siguiente = nuevo_nodo
  
  def __str__(self):
    resultado = []
    nodo = self.head
    while nodo:
      resultado.append(str(nodo.valor))
      nodo = nodo.siguiente
    return ' '.join(resultado)
def minCoins(cantidad):
  monedas = LinkedList()
  # mientras quede una cantidad por cubrir
  while cantidad > 0:
    # elegir la moneda o billete más grande disponible
    for moneda in [1000, 500, 100, 50, 20, 10, 5, 2, 1]:
      if cantidad >= moneda:
        monedas.append(moneda)
        cantidad -= moneda
        break
  # devolver la lista enlazada de monedas y billetes elegidos
  return monedas

print(minCoins(15)) # debería imprimir "10 5"
print(minCoins(27)) # debería imprimir "20 5 2"



def test_minCoins():
  # Crea una lista de pruebas y sus resultados esperados
  test_cases = [
    (15, [10, 5]),
    (27, [20, 5, 2]),
    (70, [50, 20]),
    (121, [100, 20, 1]),
    (0, [])
  ]

  # Itera sobre la lista de pruebas
  for test in test_cases:
    amount, expected_output = test
    # Verifica que la función minCoins devuelva el resultado esperado
    assert minCoins(amount) == expected_output