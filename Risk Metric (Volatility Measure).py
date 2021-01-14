import numpy as np
import pandas as pd



def risk_metric():
    df = pd.read_csv("sp500_log_returns.csv", index_col="Date")
    df.fillna(0, inplace=True)
    df.replace("",0, inplace=True)
    # list with tickers in this csv
    ticker_List = df.columns
    # list with dates
    dates = list(df.index)
    n = len(dates)

    ###DECLARE SMOOTHING PARAMETER For RiskMetrics™, Daily Data (1 year)###
    lmbd = 0.94
    thorizon =256
    #empty dataframe of size dates*ticker_List

    rm = pd.DataFrame(np.nan,index= ["RiskMetric™"], columns=ticker_List)


    denom = 0
    for i in range(thorizon):
        denom += lmbd**i

    #print(denom)
    print(df.loc[dates[n-265],"MMM"])

    for ticker in ticker_List:
        rm.loc["RiskMetric™", ticker] = 0
        for t in range(thorizon):
            if df.loc[dates[n-t-1],ticker] == 100:
                rm.loc["RiskMetric™", ticker] += 0
            else:
                rm.loc["RiskMetric™", ticker] += (lmbd**t)*(df.loc[dates[n-t-1], ticker]**2)/denom

    print(rm.loc["RiskMetric™", "MMM"])

    rm.to_csv("RiskMetrics.csv")

