1: import pybithumb
2:  
3: df = pybithumb.get_ohlcv("BTC")
4: df['range'] = (df['high'] - df['low']) * 0.5
5: df.to_excel("btc.xlsx")