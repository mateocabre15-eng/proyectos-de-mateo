import yfinance as yf
import numpy as np
import pandas as pd
# Este proyecto se trata de un analizador de portafolios, usando datos históricos de yfinance
class Portafolio():
    def __init__(self, posiciones_iniciales):
        self.posiciones = posiciones_iniciales
        self.datos_historicos = None
        self.pesos = None
        self.retorno_esperado = None
        self.matriz_covarianzas= None
        self.weights_optimos = None
        self.var_min_portafolio = None

    def descargar_datos(self):
        lista_tickers = [item["ticker"] for item in self.posiciones]
        datos_anuales = yf.download(lista_tickers, period="1y")['Close']
        self.datos_historicos = datos_anuales

    def calcular_pesos(self):
        precios_actuales = self.datos_historicos.iloc[-1]
        valor_total_cartera = 0
        valores_individuales = {}
        
        for item in self.posiciones:
            ticker = item["ticker"]
            cantidad = item["cantidad"]
            precio_accion = precios_actuales[ticker] 
            valor_posicion = cantidad * precio_accion          
            valores_individuales[ticker] = valor_posicion
            valor_total_cartera += valor_posicion

        self.pesos = {}
        for ticker, valor in valores_individuales.items():
            self.pesos[ticker] = valor / valor_total_cartera

    def calcular_retorno_historico(self):
        retorno_esperado_total = 0
        
        datos_anuales = self.datos_historicos
        retorno_total_ultimo_año = (datos_anuales.iloc[-1] / datos_anuales.iloc[0]) - 1
        
        for item in self.posiciones:
            ticker = item["ticker"]
            weight_individual = self.pesos[ticker]
            retorno_individual = retorno_total_ultimo_año[ticker]
            retorno_esperado_total += (weight_individual * retorno_individual)
            
        self.retorno_esperado = retorno_esperado_total
    def calcular_matriz_covarianzas(self):
        retornos_porcentuales = self.datos_historicos.pct_change().dropna()

        matriz = retornos_porcentuales.cov() * 252
        self.matriz_covarianzas = matriz

    def portafolio_minima_varianza(self):
        sigma = self.matriz_covarianzas.values
        n=sigma.shape[0] # estos van a ser la cantidad de weights a calcular
        unos = np.ones(n)

        weight_optimo_numerador = np.linalg.solve(sigma, unos)
        weight_optimo_denominador = np.dot(unos.T, weight_optimo_numerador)
        weight_optimo = weight_optimo_numerador/weight_optimo_denominador
        self.weights_optimos = weight_optimo
    def riesgo_portafolio_minima_var(self):
        sigma = self.matriz_covarianzas.values
        w = self.weights_optimos
        varianza = w.T @ sigma @ w
        riesgo = np.sqrt(varianza)
        self.var_min_portafolio = riesgo
        
acciones = {
    # Wall Street
    "apple": "AAPL",
    "microsoft": "MSFT",
    "tesla": "TSLA",
    "google": "GOOGL",
    "amazon": "AMZN",
    "meta": "META",
    "nvidia": "NVDA",
    "netflix": "NFLX",
    "jpmorgan": "JPM",
    "goldman": "GS",
    "berkshire": "BRK-B",
    "johnson": "JNJ",
    "visa": "V",
    "mastercard": "MA",
    "coca cola": "KO",
    "pepsi": "PEP",
    "mcdonalds": "MCD",
    "disney": "DIS",
    "boeing": "BA",
    "exxon": "XOM",
    "chevron": "CVX",
    "pfizer": "PFE",
    "uber": "UBER",
    "airbnb": "ABNB",
    "spotify": "SPOT",
    "paypal": "PYPL",
    "intel": "INTC",
    "amd": "AMD",
    "salesforce": "CRM",
    "oracle": "ORCL",

    # acciones de argentina
    "galicia": "GGAL.BA",
    "macro": "BMA.BA",
    "pampa": "PAMP.BA",
    "ypf": "YPFD.BA",
    "mercadolibre": "MELI.BA",
    "telecom": "TECO2.BA",
    "loma negra": "LOMA.BA",
    "ternium": "TXAR.BA",
    "aluar": "ALUA.BA",
    "cresud": "CRES.BA",
    "irsa": "IRSA.BA",
    "supervielle": "SUPV.BA",
    "bbva argentina": "BBAR.BA",
    "transportadora": "TGSU2.BA",
    "central puerto": "CEPU.BA",
    "edenor": "EDN.BA",
    "metrogas": "METR.BA",
    "molinos": "MOLI.BA",
    "agrometal": "AGRO.BA",
    "holcim": "JMIN.BA",
}

portafolio=[]
while True:
    ticker= input("acciones del portafolio, escribir 'termine' cuando anotes todas: ").strip().lower()
    if ticker=="termine": 
        break
    accion=acciones.get(ticker, ticker).upper()
    info_ticker=yf.Ticker(accion)

    if info_ticker.history(period="1d").empty: print("No encontré ese ticker.")
    try:

        cantidad = int(input(f"¿Cuántas acciones de {accion} tienes?: "))
        portafolio.append({"ticker": accion, "cantidad": cantidad})
    except ValueError: print("pone numero")

mi_cartera = Portafolio(posiciones_iniciales=portafolio)
print("--Procediendo a descargar datos anuales de YFinance...--")

mi_cartera.descargar_datos()
mi_cartera.calcular_pesos()
mi_cartera.calcular_retorno_historico()
mi_cartera.calcular_matriz_covarianzas()
mi_cartera.portafolio_minima_varianza()
mi_cartera.riesgo_portafolio_minima_var()
print("------------------------------------------------")
print(f"El retorno esperado histórico es de {mi_cartera.retorno_esperado:.2%}")
print(f"Portafolio mínima varianza:")
tickers_ordenados = mi_cartera.datos_historicos.columns
for ticker, peso in zip(tickers_ordenados, mi_cartera.weights_optimos):
    if peso>0.001:
        print(f" - {ticker}: {peso:.2%}")
print(f"Esta cartera tiene un riesgo del {mi_cartera.var_min_portafolio:.2%}")
print("------------------------------------------------")