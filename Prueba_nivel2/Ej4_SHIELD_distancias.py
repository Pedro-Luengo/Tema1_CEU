import heapq

def dijkstra(grafo, start):
  distancias = {node: float('inf') for node in grafo}
  distancias[start] = 0
  cola = [(0, start)]
  predecesor = {start: None}
  
  while cola:
    distancia, node = heapq.heappop(cola)
    
    if distancia == distancias[node]:
      for vecino in grafo[node]:
        new_distancia = distancia + grafo[node][vecino]
        if new_distancia < distancias[vecino]:
          distancias[vecino] = new_distancia
          predecesor[vecino] = node
          heapq.heappush(cola, (new_distancia, vecino))
          
  return predecesor, distancias

# Ejemplo de uso

grafo = {
  'Nick Fury': {'Iron Man': 675, 'The Incredible Hulk': 400, 'Khan': 166, 'Thor': 809, 'Captain America': 720, 'Ant-Man': 399, 'The Winter Soldier': 233},
  'Iron Man': {'Nick Fury': 675, 'The Incredible Hulk': 540, 'Khan': 107, 'Thor': 111, 'Captain America': 206, 'Ant-Man': 155, 'The Winter Soldier': 621},
  'The Incredible Hulk': {'Nick Fury': 400, 'Iron Man': 540, 'Khan': 687, 'Thor': 179, 'Captain America': 348, 'Ant-Man': 199, 'The Winter Soldier': 401},
  'Khan': {'Nick Fury': 166, 'Iron Man': 107, 'The Incredible Hulk': 687, 'Thor': 752, 'Captain America': 521, 'Ant-Man': 385, 'The Winter Soldier': 280},
  'Thor': {'Nick Fury': 809, 'Iron Man': 111, 'The Incredible Hulk': 179, 'Khan': 752, 'Captain America': 540, 'Ant-Man': 990, 'The Winter Soldier': 361},
  'Captain America': {'Nick Fury': 720, 'Iron Man': 206, 'The Incredible Hulk': 348, 'Khan': 521, 'Thor': 540, 'Ant-Man': 412, 'The Winter Soldier': 576},
  'Ant-Man': {'Nick Fury': 399, 'Iron Man': 155, 'The Incredible Hulk': 199, 'Khan': 385, 'Thor': 990, 'Captain America': 412, 'The Winter Soldier': 621},
  'The Winter Soldier': {'Nick Fury': 233, 'Iron Man': 621, 'The Incredible Hulk': 401, 'Khan': 280, 'Thor': 361, 'Captain America': 576, 'Ant-Man': 621}
}

predecesor, distancias = dijkstra(grafo, 'Nick Fury')

# Imprimir el recorrido completo
nodo = 'Nick Fury'
path = []
while predecesor[nodo] is not None:
  path.append(nodo)
  node = predecesor[nodo]
path.append(nodo)
print(path[::-1])

# Imprimir las distancias más cortas
print(distancias)