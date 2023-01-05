def potencia(base, exponente):
    # Caso base: cuando el exponente es 0, la potencia es 1
    if exponente == 0:
        return 1
    
    # Si el exponente es par, calcular la potencia de la base elevada al exponente / 2 y multiplicarla por sí misma
    if exponente % 2 == 0:
        return potencia(base, exponente // 2) * potencia(base, exponente // 2)
    
    # Si el exponente es impar, calcular la potencia de la base elevada al exponente - 1 y multiplicarla por la base
    return base * potencia(base, exponente - 1)

if __name__ == "__main__":
    print(potencia(2, 5))  # Imprime 32
    print(potencia(2, 6))  # Imprime 64
    print(potencia(3, 3))  # Imprime 27
    print(potencia(3, 4))  # Imprime 81