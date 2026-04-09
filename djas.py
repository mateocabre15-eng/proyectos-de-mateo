import yfinance as yf

acciones = {"apple": "AAPL", "microsoft": "MSFT", "galicia": "GGAL"}
portafolio = []

while True:
    entrada = input("\nAcción (o 'termine'): ").strip().lower()
    if entrada == "termine": 
        break
    
    print(f"--> DEBUG 1: Tú escribiste: '{entrada}'")
    
    ticker_a_buscar = acciones.get(entrada, entrada).upper()
    print(f"--> DEBUG 2: Lo que le enviamos a Yahoo es: '{ticker_a_buscar}'")
    
    info_ticker = yf.Ticker(ticker_a_buscar)
    historial = info_ticker.history(period="1d")
    
    if historial.empty:
        print(f"❌ No encontré ese ticker: '{ticker_a_buscar}'.")
        continue 
    
    print(f"✅ ¡Éxito! Yahoo Finance encontró '{ticker_a_buscar}'.")
    
    try:
        cantidad = int(input(f"¿Cuántas acciones de {ticker_a_buscar} tienes?: "))
        portafolio.append({"ticker": ticker_a_buscar, "cantidad": cantidad})
    except ValueError:
        print("⚠️ Error: Debes poner un número entero.")

print(f"\nPortafolio final: {portafolio}")