import os
import yfinance as yf
import pandas as pd

def get_data_for_ticker(ticker, **kwargs):
    ''' pull historical data from yahoo finance '''
    stock_split = 0
    start_date = kwargs.get('start_date', pd.Timestamp.today() - pd.Timedelta(days=365))
    tmp = yf.Ticker(ticker)
    tmp1 = tmp.history(start=start_date)
    if tmp1['Stock Splits'].sum() > 0:
        stock_split=1
    return tmp1.loc[:,['Close']], stock_split