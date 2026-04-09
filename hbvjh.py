import yfinance as yf


nombre_accion = input("¿a que acción le calculamos el CAPM?: ")
tasa_libre_riesgo = 0.042  
premio_mercado = 0.06      

accion = yf.Ticker(nombre_accion)
beta = accion.info.get('beta')

if beta is not None:
    retorno_esperado = tasa_libre_riesgo + (beta * premio_mercado)
    
    print("---")
    print(f"📊 Análisis de CAPM para {nombre_accion.upper()}:")
    print(f"Beta encontrada: {beta}")
    print(f"Costo del Capital Propio (Ke): {retorno_esperado * 100:.2f}%")
else:
    print(f"No pudimos encontrar la Beta para {nombre_accion}. Probá con otra.")