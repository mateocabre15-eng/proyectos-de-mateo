# --- Ejercicio 1 ---
"""valor_nominal = 1000
tasa_cupon = 0.08
rendimiento_exigido = 0.1
c = valor_nominal*tasa_cupon
valor_presente = 0
for i in range(1, 6):
    a = c/(1+rendimiento_exigido)**i
    valor_presente+= round(a, 2)
b = valor_nominal/(1+rendimiento_exigido)**5
valor_presente += b
print("----------------")
print(f"El valor presente del bono es {valor_presente}")"""

# ---Ejercicio 2---
"""tasa1 = 0.04
tasa2 = 0.045
tasa_forward = (1+tasa2)**2/(1+tasa1) -1
print(f"La tasa forward implícita a 1 año, dentro de 1 año, es de: {tasa_forward:.2%}")"""

# ---Ejercicio 3---
"""capital_inicial = 1000000
tna = 0.6
n = 90/30
m = 12
valor_final = capital_inicial*(1+tna/m)**n
tasa_plazo_fijo = (1+tna/m)**n

pagare = 1160000
valor_presente = pagare*(1/(tasa_plazo_fijo))
print("-----------------")
print(f"El valor presente del pagaré es de {round(valor_presente, 3)} y el valor final del plazo fijo es de {round(valor_final, 2)}")
if valor_final > pagare:
    print("Te conviene el plazo fijo")
else: print("Te conviene el pagaré")"""

# --- Ejercicio 15 ---
"""tasa = 0.076
año1 = 2/(1+tasa)
año2 = 3/(1+tasa)**2
año3 = 5.4/(1+tasa)**3
año4 = 5.8/(1+tasa)**4
monto_total = año1+año2+año3+año4
print(round(monto_total, 2))"""

# --- Ejercicio 16 ---
"""tasa = 0.05
año1 = 0.03
año2 = 0.04
precio = 5/(1+año1) + 105/(1+año2)**2
print(round(precio, 2))"""