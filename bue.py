
portfolio = {
    "GGAL": 3200.50,
    "YPFD": 5100.00,
    "PAMP": 2900.20,
    "BMA": 4500.75
}

ticker_maximo = ""
precio_maximo = 0

for ticker, precio in portfolio.items():
    print(f"Analizando {ticker} a ${precio}...")
    
    if precio > precio_maximo:
        precio_maximo = precio
        ticker_maximo = ticker

print("---")
print(f"🚀 Resultado final: La acción más cara es {ticker_maximo} con ${precio_maximo:.2f}")