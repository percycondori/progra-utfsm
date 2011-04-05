def sumar(n, f):
    s = 0
    for i in range(n):
        s = s + f(i)
    return s

def identidad(x):
    return x

def cuadrado(x):
    return x ** 2

def cubo(x):
    return x ** 3

print suma(1000, identidad)
print suma(1000, cuadrado)
print suma(1000, cubo)
