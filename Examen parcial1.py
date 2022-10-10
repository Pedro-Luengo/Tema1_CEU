import sys
"""sys.path(0,"lugar de la ruta")"""

def fibonacciR(n):
    """Calculo de fibonacci recursivo"""
    if(n == 0 or n == 1):
        return n
    else:
        return fibonacciR(n-1) + fibonacciR(n-2)
fibonacciR(32)