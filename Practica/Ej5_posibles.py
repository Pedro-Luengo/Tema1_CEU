def minimo_num_monedas(valor: int):
    # Definir la lista de monedas y billetes disponibles
    monedas = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    
    # Contador de monedas y billetes necesarios
    num_monedas = 0
    
    # Lista de monedas y billetes utilizados
    monedas_usadas = []
    
    # Mientras haya cambio por dar, seguir buscando monedas y billetes
    while valor > 0:
        # Encontrar la moneda o billete más grande disponible que sea menor o igual al valor de cambio
        moneda = max([c for c in monedas if c <= valor])
        # Restar el valor de la moneda o billete al valor de cambio
        valor -= moneda
        # Aumentar en 1 el contador de monedas y billetes necesarios
        num_monedas += 1
        # Añadir la moneda o billete a la lista de monedas y billetes utilizados
        monedas_usadas.append(moneda)
    
    # Devolver el contador de monedas y billetes necesarios y la lista de monedas y billetes utilizados
    return num_monedas, monedas_usadas

# Pruebas
if __name__ == "__main__":
    print(minimo_num_monedas(0))   # Debe imprimir (0, [])
    print(minimo_num_monedas(70))  # Debe imprimir (2, [50, 20])
    print(minimo_num_monedas(121))  # Debe imprimir (3, [100, 20, 1])
    print(minimo_num_monedas(442))  # Debe imprimir (3, [100, 100, 100, 100, 20, 20, 2])