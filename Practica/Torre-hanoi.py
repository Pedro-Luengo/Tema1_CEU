movimientos = 0

def resolver_torre_hanoi(n, origen, destino, auxiliar, movimientos):
    if n == 1:
        movimientos += 1
    else:
        movimientos = resolver_torre_hanoi(n-1, origen, auxiliar, destino, movimientos)
        movimientos += 1
        movimientos = resolver_torre_hanoi(n-1, auxiliar, destino, origen, movimientos)
    return movimientos

movimientos = resolver_torre_hanoi(20, "origen", "destino", "auxiliar", movimientos)
print(f"Se han realizado {movimientos} movimientos")