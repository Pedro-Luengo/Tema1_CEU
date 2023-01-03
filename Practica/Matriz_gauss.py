matriz = []

def crear_matriz(n):
    for i in range (n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(0)
    return matriz

def rellenar(n):
    matriz = crear_matriz(n)
    for x in range(n):
        for y in range(n):
            matriz[x][y] = int(input("Valor de [" + str(x) + "][" + str(y) + "] = "))
    return matriz

def gauss(n, matriz):
    for z in range(n-1):
        for x in range(1, n-z):
            if (matriz[z][z] != 0):
                p = matriz[x+z][z] / matriz[z][z]
                for y in range(n):
                    matriz[x+z][y] = matriz[x+z][y] - (matriz[z][y]*p)

def determinante(n, matriz):
    determinante = 1
    for x in range(n):
        determinante = matriz[x][x]*determinante
    print("\nEl determinante de la matriz es = ", determinante)

n = int(input("Tamaño de la matriz : "))
matriz = rellenar(n)
gauss(n, matriz)
determinante(n, matriz)