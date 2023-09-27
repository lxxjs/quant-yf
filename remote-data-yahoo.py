import urllib3
import pandas_datareader.data as web
import yfinance as yf
import pandas as pd
import datetime as dt
urllib3.disable_warnings()

tday = dt.datetime.today()

#df = yf.download('GE', start='2020-01-01', end=tday)

TSLA = yf.Ticker('tsla')
AAPL = yf.Ticker('aapl')
GOOG = yf.Ticker('goog')
ORC = yf.Ticker('ORC')
KO = yf.Ticker('ko')

print(KO.info['dividendRate'])