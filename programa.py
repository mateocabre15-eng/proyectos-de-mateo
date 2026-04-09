precio_actual = float(input("¿A cuánto está el ADR de Galicia hoy? "))

if precio_actual < 30.5:
    print("¡COMPRAR! Está barato.")
elif precio_actual > 35.0:
    print("VENDER. Momento de tomar ganancias.")
else:
    print("MANTENER. No hagas nada.")