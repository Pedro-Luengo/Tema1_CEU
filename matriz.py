matriz = []

def crear_matriz(numero):
    for i in range (numero):
        matriz.append([])
        for j in range (numero):
            matriz[i].append(0)
    return matriz

def rellenar(numero):
    matriz = crear_matriz(numero)
    for x in range (numero):
        for y in range (numero):
            matriz[x][y] = float(input('Valor de [' + str(x) + '][' + str(y) + '] = '))

numero = int(input ('Cual es el tamaño de la matriz : '))
rellenar(numero)
print(f"{matriz[0]}\n{matriz[1]}\n {matriz[2]}\n{matriz[3]}\n{matriz[4]}\n")