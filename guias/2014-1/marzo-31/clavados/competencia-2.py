nombre_ganador = ''
puntaje_ganador = 0.0

while True:
    nombre = raw_input('Nombre: ')
    if nombre == 'FIN':
        break
    dif = float(raw_input('Grado de dificultad: '))
    suma = 0.0
    menor = 10.0
    mayor = 0.0
    for i in range(7):
        salto = float(raw_input('Juez ' + str(i + 1) + ': '))
        suma += salto
        menor = min(menor, salto)
        mayor = max(mayor, salto)
    total = (3.0 / 5.0) * (suma - menor - mayor) * dif

    if total > puntaje_ganador:
        puntaje_ganador = total
        nombre_ganador = nombre

print 'El ganador es', nombre_ganador
