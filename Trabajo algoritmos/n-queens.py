"""
 El problema se resuelve situando N reinas en un tablero de ajedrez de NxN de tal forma que ninguna de las reinas se amenace entre sí
Esto significa que ninguna reina puede tener a otra reina en su horizontal, vertical y diagonal.

"""
from __future__ import annotations

solution = []


def is_safe(board: list[list[int]], row: int, column: int) -> bool:
    """
    Esta función devuelve un booleano (verdadero o falso) en funcionde si la reina esta a salvo o no.    

    """
    for i in range(len(board)):
        if board[row][i] == 1:
            return False
    for i in range(len(board)):
        if board[i][column] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, len(board))):
        if board[i][j] == 1:
            return False
    return True


def solve(board: list[list[int]], row: int) -> bool:
    """
    Crea un árbol de espacio de estado y llama a la función segura hasta que recibe un
    Falso Booleano y termina esa rama y retrocede a la siguiente
    posible rama de solución.
    """
    if row >= len(board):
        """
       Si el número de fila excede N, tenemos un tablero con una combinación exitosa
        y esa combinación se agrega a la lista de soluciones y se imprime el tablero.

        """
        solution.append(board)
        printboard(board)
        print()
        return True
    for i in range(len(board)):
        """
        Para cada fila itera a través de cada columna para verificar si es factible
        coloca una reina allí.
        Si todas las combinaciones para esa rama en particular tienen éxito, el tablero es
        reinicializará para la siguiente combinación posible.
        """
        if is_safe(board, row, i):
            board[row][i] = 1
            solve(board, row + 1)
            board[row][i] = 0
    return False


def printboard(board: list[list[int]]) -> None:
    """
    Imprime los tableros que tienen una combinación exitosa.
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# n= numero de reinas
n = 5
board = [[0 for i in range(n)] for j in range(n)]
solve(board, 0)
print("El numero total de soluciones es: ", len(solution))