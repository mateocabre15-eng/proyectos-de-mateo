import yfinance as yf
import pandas as pd

activo = 'AAPL'
mercado = '^GSPC'
bono = '^TNX'

print(f"bajando la data de {activo}...")

df = yf.download([activo, mercado, bono], start='2021-01-01', end='2024-01-01')['Adj Close']

rf = df[bono].iloc[-1] / 100

rets = df[[activo, mercado]].pct_change().dropna()

rm = rets[mercado].mean() * 252

beta = rets[activo].cov(rets[mercado]) / rets[mercado].var()

capm = rf + beta * (rm - rf)

print("---")
print(f"rf: {rf:.4f}")
print(f"rm: {rm:.4f}")
print(f"beta: {beta:.4f}")
print("---")
print(f"capm esperado: {capm:.4f}")