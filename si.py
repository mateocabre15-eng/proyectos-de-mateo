precios = [120, 125, 122, 128, 130]
suma_filtros = 0
cantidad_caros = 0 # <-- Este es nuestro contador
precio_max = 0

limite = float(input("que precio limite queres?"))

for precio in precios:
    if precio > limite:
        suma_filtros += precio
        cantidad_caros += 1 # <-- Sumamos 1 unidad, no el precio
        print(f"Encontré uno: {precio}")
    if precio > precio_max:
        precio_max = precio
        print(f"nuevo record: {precio_max}")

print("---")
print(f"Total sumado: {suma_filtros}")
print(f"Cantidad encontrada: {cantidad_caros}")
print(f"El precio más alto encontrado fue: {precio_max}")

# BONUS: Calcular el promedio de los caros
if cantidad_caros > 0:
    promedio_caros = suma_filtros / cantidad_caros
    print(f"El promedio de los caros es: {promedio_caros}")



