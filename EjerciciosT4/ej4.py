import doctest

def biseccion(f, a, b, epsilon):
    iteraciones = 0
    while abs(a - b) > epsilon:
        iteraciones += 1
        m = (a + b) / 2
        if f(m) == 0:
            return m
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2, iteraciones


def secante(f, x0, epsilon):
    iteraciones = 0
    x1 = x0 - f(x0) / derivative(f, x0, epsilon)
    while abs(x1 - x0) > epsilon:
        iteraciones += 1
        x0 = x1
        x1 = x0 - f(x0) / derivative(f, x0, epsilon)
    return x1, iteraciones

def derivative(f, x, h):
  return (f(x + h) - f(x)) / h


def newton_raphson(f, df, x0, epsilon):
    iteraciones = 0
    x1 = x0 - f(x0) / df(x0)
    while abs(x1 - x0) > epsilon:
        iteraciones += 1
        x0 = x1
        x1 = x0 - f(x0) / df(x0)
    return x1, iteraciones

# Define la función f(x)
def f(x):
  return x**3 + x +16 
# Define la derivada de la función f(x)
def df(x):
  return 3*x**2 + 1

# Encuentra una raíz de f(x) con una precisión de 10^-5
if __name__ == '__main__':
    doctest.testmod()
    # Encuentra una raíz de f(x) con una precisión de 10^-5
    print(biseccion(f, 0, 4, 10**-5))
    # Encuentra una raíz de f(x) con una precisión de 10^-5
    print(secante(f, 1, 10**-5))
    # Encuentra una raíz de f(x) con una precisión de 10^-5
    print(newton_raphson(f, df, 1, 10**-5))