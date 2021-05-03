 import time
 import pybithumb
 import datetime
 
 def get_target_price(ticker):
     df = pybithumb.get_ohlcv(ticker)
     yesterday = df.iloc[-2]
 
     today_open = yesterday['close']
     yesterday_high = yesterday['high']
     yesterday_low = yesterday['low']
     target = today_open + (yesterday_high - yesterday_low) * 0.5
     return target
 
 now = datetime.datetime.now()
 mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
17: target_price = get_target_price(“BTC”)
18: 
19: while True:
20:     now = datetime.datetime.now()
21:     if mid < now < mid + datetime.delta(seconds=10) : 
22:         target_price = get_target_price(“BTC”)
23:         mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
24: 
25:     current_price = pybithumb.get_current_price("BTC")
26:     print(current_price)
27: 
28:     time.sleep(1)