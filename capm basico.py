tasaf = float(input("cual es la tasa libre de riesgo?"))
prima_de_riesgo = float(input("cual es la prima de riesgo?"))
beta = float(input("cual es la beta?"))

retorno_esperado = tasaf + (prima_de_riesgo * beta)

print(f"el retorno esperado es de {retorno_esperado:.2f}")
