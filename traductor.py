import yfinance as yf
import numpy as np

TRADUCTOR = {
    "apple": "AAPL",
    "google": "GOOGL",
    "galicia": "GGAL",
    "tesla": "TSLA"
}

def calcular_beta(accion, periodo="1y"):
    accion_hist = accion.history(period=periodo)['Close']
    mercado = yf.Ticker("^GSPC").history(period=periodo)['Close']
    
    retornos_accion = accion_hist.pct_change().dropna()
    retornos_mercado = mercado.pct_change().dropna()
    
    retornos_accion, retornos_mercado = retornos_accion.align(retornos_mercado, join='inner')
    
    covarianza = np.cov(retornos_accion, retornos_mercado)[0][1]
    varianza_mercado = np.var(retornos_mercado)
    
    return covarianza / varianza_mercado

def obtener_datos_financieros():
    entrada = input("¿Qué acción querés mirar hoy? ").strip().lower()
    ticker_symbol = TRADUCTOR.get(entrada, entrada).upper()
    print(f"\nBuscando datos para: {ticker_symbol}...")
    
    accion = yf.Ticker(ticker_symbol)
    
    try:
        historial = accion.history(period="1d")
        
        if historial.empty:
            print(f"Error: No se encontraron datos para '{ticker_symbol}'.")
            return
        
        ultimo_cierre = historial['Close'].iloc[-1]
        print("-" * 30)
        print(f"El precio actual de {ticker_symbol} es: ${ultimo_cierre:.2f}")
        
        decision = input("\n¿Querés calcular su CAPM? (si/no): ").lower()
        if decision == "si":
            tasa_libre_riesgo = 0.042
            prima_riesgo_mercado = 0.06
            
            print("\nCalculando beta desde datos históricos...")
            beta = calcular_beta(accion)
            
            retorno_esperado = tasa_libre_riesgo + (beta * prima_riesgo_mercado)
            
            print(f"\nResultados para {ticker_symbol}:")
            print(f"  • Beta (calculado): {beta:.2f}")
            print(f"  • Retorno esperado (CAPM): {retorno_esperado * 100:.2f}%")
            
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    obtener_datos_financieros()
else:
    print("ok chau")
    
    