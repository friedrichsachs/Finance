import math
import numpy as np
import pandas as pd
import scipy.stats as st

def VaR_parametric(alpha, ticker, amount_at_risk):
    #import dataset with historical log returns
    df = pd.read_csv("sp500_log_returns.csv", index_col="Date")
    tickers = df.columns
    dates = list(df.index)
    n = len(df[ticker])

    zalpha = -st.norm.ppf(1-alpha)
    std = df[ticker].std()
    twosigma =(1+2*(2/n)**0.5)**0.5
    VaR_para = zalpha*std*twosigma*amount_at_risk
    print(VaR_para)
    return VaR_para

VaR_parametric(0.05, "AAPL", 10000)
