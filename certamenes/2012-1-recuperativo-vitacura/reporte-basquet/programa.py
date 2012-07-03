'''
>>> calcular_puntos('DLLDTL')
10
'''


def calcular_puntos(anotaciones):
    return (anotaciones.count('L') +
            anotaciones.count('D') * 2 +
            anotaciones.count('T') * 3)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

