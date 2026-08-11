Financial & Quantitative Projects in Python

Welcome to my financial analytics repository. This space contains a collection of Python-based scripts, Jupyter notebooks, and quantitative models developed during my undergraduate studies in Finance at UADE. The projects focus on financial modeling, econometrics, portfolio optimization, and market data processing.

---

Projects Overview

1. Automated CAPM Calculation & Asset Valuation
* File: `modelo_capm.py`
* Description: An automated Python script designed to compute Capital Asset Pricing Model (CAPM) parameters for equity valuation.
* Key Features:
  * Automated data retrieval and equity beta estimation against market benchmarks.
  * Integration of real-time market data via `yfinance`.
  * Data cleaning logic and risk-free rate management.
* Tech Stack: Python, Pandas, NumPy, YFinance.

2. Portfolio Optimization & Efficient Frontier Analysis
* File: `Analisis de Portafolio.py`
* Description: Quantitative script for portfolio risk analysis, variance evaluation, and Minimum Variance Portfolio (MVP) construction.
* Key Features:
  * Covariance matrix estimation and annualized return/volatility metrics.
  * Efficient frontier plotting and optimal asset weight allocations.
* Tech Stack: Python, NumPy, Pandas, Plotly, YFinance.

3. Econometric Analysis of Corporate Bond Credit Spreads
* File: `Challenge Econometría.ipynb`
* Description: An empirical econometric study modeling the relationship between U.S. corporate bond credit spreads and macroeconomic drivers.
* Data Sources (`.csv`): Incorporates historical FRED market metrics including 10-Year Treasury Constant Maturity (`DGS10.csv`), 10-Year to 2-Year Treasury Yield Spread (`T10Y2Y.csv`), CBOE Volatility Index (`VIXCLS.csv`), S&P 500 Index (`SP500.csv`), and Corporate Credit Spreads (`spreads.csv`).
* Key Features:
  * Multiple Linear Regression (OLS estimation) evaluating bond spreads against yield curve slope, volatility, and equity levels.
  * Hypothesis testing, diagnostic checks, and log-log elasticity analysis.
* Tech Stack: Python, Jupyter Notebook, Pandas, Statsmodels, Matplotlib / Seaborn.

---

Repository Structure

```text
├── .gitignore
├── Analisis de Portafolio.py
├── Challenge Econometría.ipynb
├── DGS10.csv
├── README.md
├── SP500.csv
├── T10Y2Y.csv
├── VIXCLS.csv
├── modelo_capm.py
└── spreads.csv
