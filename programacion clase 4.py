#programacion clase 4

# ejercicio 1

"""
cat = input("ingrese categoria: ")

edad = int(input("edad: "))

if cat.lower()=="a" or 10<edad<20: print("socio vip")
else: print("no es socio vip")

print("***Fin del programa***")
"""

# ejercicio 2

"""
horas_trabajadas = int(input("Cuantas horas trabajaste? "))
categoria = int(input("categoria? "))

if categoria == 1: sueldo = horas_trabajadas*200
elif categoria == 2: sueldo = horas_trabajadas*300
elif categoria == 3: sueldo = horas_trabajadas*400
else: print("pone un numero entre 1 y 3")
print(f"Tu sueldo es {sueldo}")
"""

# ejercicio 3

"""
num = int(input("numero "))
if num % 2 == 0: print("par") 
else: print("impar")
"""

# ejercicio 4
"""
num = int(input("numero "))
if num % 7 == 0 and num > 40: print(True)
else: print(False)
"""

# ejercicio 5
"""
num= int(input("numero entre 1 y 50 "))
if num>50 or num<1: print("que sea entre 1 y 50")
else: print(num+1)
"""

# ejercicio 6

"""
import random as rd

numero = rd.randint(0, 200)
print(numero)
print(round(numero*1.3, 2))
print("***Fin del Programa***")
"""

# ejercicio 7

"""
base = int(input("base? "))
alt = int(input("altura? "))
area= base*alt
perim = base*2 + alt*2
print("---------------------")
print(f"el area es de {area}")
print(f"el perimetro es de {perim}")
print("*** Fin del Programa ***")
print("---------------------")
"""

# ejercicio 8

"""
hombres = int(input("cantidad de hombres "))
mujeres = int(input("cantidad de mujeres "))

print(f"El porcentaje de hombres es {round(hombres/(hombres+mujeres)*100, 2)} y el porcentaje de mujeres es {round(mujeres/(mujeres+hombres)*100, 2)}")
"""

# ejercicio 9

"""
antiguedad = int(input("cual es la antiguedad del empleado? "))
sueldo = int(input("cual es su salario? "))

if antiguedad < 1:
    paga= sueldo
elif 1<=antiguedad<=3:
    paga = sueldo*1.05
elif 4<= antiguedad<=6:
    paga= sueldo*1.1
else:
    paga = sueldo*1.2

print(f"la paga sera de {paga}")
"""
# ---------------------------------------------------------
# Ejercicios Bucles For

# Ejercicio 1

"""
cuad= 0
for i in range(1, 11):
    cuad += i**2
print(cuad)
"""

# Ejercicio 3

"""
numeros_grandes = 0
for i in range(1, 11):
    num = int(input("ingresa numero "))
    if num>4:
        numeros_grandes += 1
print(f"la cantidad de numeros mayores a 4 es {numeros_grandes} ")
"""

"""
# Ejercicio 4
c = 0
for i in range(1, 16):
    nota_alumno = int(input("nota "))
    if nota_alumno >7:
        c += 1
print(f"cantidad de aprobados es {c}")
"""

"""
# Ejercicio 5
c = 0
for i in range(1, 21):
    num = int(input("num "))
    if num < 15:
        c += 1
print(f"el {c:.2%} de los numeros es menor a 15")
"""
