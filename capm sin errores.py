while True:
    try:
        tasa_libre_de_riesgo = float(input("cual es la tasa libre de riesgo?"))
        beta = float(input("cual es la beta?"))
        premio_mercado = float(input("cual es la recompensa del mercado?"))
        
        retorno_esperado = tasa_libre_de_riesgo + (beta * premio_mercado)
        print(f"La rentabilidad del activo es de {retorno_esperado:.2f}")
        break
    except ValueError:
        print("error: no pusiste un numero")
    
          
                                