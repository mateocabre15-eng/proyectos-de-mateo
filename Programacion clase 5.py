"""

# Ejercicio 1

n = int(input("numero "))
suma = 0
while n>=0:
    suma += n
    n = int(input("numero"))
print(suma)

"""

"""

# Ejercicio 2

n = int(input("Nota: "))
total = 0
cant = 0
while n>=0:
    total += n
    cant += 1
    n = int(input("nota: "))
print("El promedio de las notas es", round(total/cant, 2))

"""

"""

# Ejercicio 3
h = 0
while h<=100:
    print(h)
    h+=1

"""

"""

# Ejercicio 4
n = int(input("sueldo: "))
cant = 0
total = 0
while n!=0:
    total += n
    cant += 1
    n = int(input("sueldo: "))
print("el promedio de los sueldos es", round(total/cant, 2))

"""

"""

# Ejercicio 5

n = int(input("numero: "))
while n != 0:
    if n<0:
        print("negativo")
    else: print("positivo")
    n = int(input("numero: "))

"""

"""

# Ejercicio 6
n = int(input("Numero: "))
cant = 1
max = n
while cant<10:
    cant += 1
    n = int(input("numero: "))
    if n>max: max = n
print(max)

"""

"""

# Ejercicio 7

n = int(input("num: "))
cant = 1
min = n
while cant<10:
    n = int(input("num: "))
    if n < min: min = n
    cant += 1
print("el valor minimo es", min)

"""

"""

# Ejercicio 8

temp = int(input("temperatura: "))
cant_0 = 0
cant = 0
total = 0
while temp <= 50:
    total += temp
    cant += 1
    if temp == 0: cant_0 += 1
    temp = int(input("temperatura: "))
print("el promedio es:", round(total/cant, 2))
print("la cantidad de valores de 0 grados es", cant_0)

"""
