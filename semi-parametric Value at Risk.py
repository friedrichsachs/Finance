import math
import numpy as np
import pandas as pd
import scipy.stats as st


def VaR_semi_parametric(alpha, beta, ticker, amount_at_risk):
    #import dataset with historical log returns
    df = pd.read_csv("sp500_log_returns.csv", index_col="Date")
    tickers = df.columns
    dates = list(df.index)

    ranked_returns = list(df[ticker])
    ranked_returns.sort()
    n = len(ranked_returns)

    F_hat = np.linspace(0,1,n,endpoint=False)
    z_beta = -st.norm.ppf(1-beta)

    obs = n*alpha+z_beta*(n*alpha*(1-alpha))**0.5
    print(obs)

    #get nalpha-th observation
    F_r = 0
    for i in range(len(F_hat)):
        if F_hat[i] < obs:
            F_r = ranked_returns[i]
        else:
            break
    print(F_r)
    Var_non_para = math.exp(F_r-1)*amount_at_risk
    print(Var_non_para)
    return Var_non_para

VaR_semi_parametric(0.05, 0.05, "AAPL", 10000)


