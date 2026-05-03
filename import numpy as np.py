import numpy as np
pipi = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9], 
                 [10, 11, 12, 13, 14, 15, 16, 17, 18]])
# los arrays tienen que tener la misma longitud

print(pipi[1, 2] + pipi[0, 0])

""" con el [] de pipi podemos acceder a cada elemento del array,
    por cada dimension se suma un elemento que debemos especificar"""

print(pipi[::-1])

""" dentro de los arrays tambien podemos seleccionar distintas filas con :
    separando inicio:final:salto
    el salto lo que hace es ir omitiendo filas cada x veces
    recordar que el - hace que se invierta el orden"""

print(pipi[:, 2])

""" si ponemos un : se seleccionan todos los elementos de la dimension, haciendo que
    nos devuelva para cada fila (1d) la columna 2 (2d)"""

print (pipi[:, 4:]) # cada columna desde la 5ta hasta la ultima

print(pipi[0, :2])

#  ------------ Aritmética ----------