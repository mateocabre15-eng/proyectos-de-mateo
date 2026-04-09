import numpy as np
pipi = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9], 
                 [10, 11, 12, 13, 14, 15, 16, 17, 18]])
# los arrays tienen que tener la misma longitud

print(pipi[1, 2] + pipi[0, 0])

""" con el [] de pipi podemos acceder a cada elemento del array,
    por cada dimension se suma un elemento que debemos especificar"""

print(pipi[::-1])