1: import pybithumb
2:  
3: df = pybithumb.get_ohlcv("BTC")
4: print(df.tail())