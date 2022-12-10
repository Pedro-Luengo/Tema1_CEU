movimientos = {
    0: [4, 6],
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [3, 9, 0],
    5: [],
    6: [1, 7, 0],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4]
}

def movimientosposibles(inicio, pasos):
    n = 0
    if pasos:
        for proximo in movimientos[inicio]:
            print("{} : {} -> {}".format(pasos, inicio, proximo))
            n += 1 + movimientosposibles(proximo, pasos - 1)
    return n

def totalizar(pasos):
    total = 0
    for i in range(10):
        total += movimientosposibles(i, pasos)
    return total

def resultado(num):
    result = totalizar(num) - totalizar(num - 1)
    return result

print(resultado(3))