# ch06/06_20.py
# 코드 생략
32: def get_yesterday_ma5(ticker):
33:     df = pybithumb.get_ohlcv(ticker)
34:     close = df['close']
35:     ma = close.rolling(5).mean()
36:     return ma[-2]
37: 
38: now = datetime.datetime.now()
39: mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
40: ma5 = get_yesterday_ma5("BTC")
41: target_price = get_target_price(“BTC”)
42:
43: while True:
44:     try:
45:         now = datetime.datetime.now()
46:         if mid < now < mid + datetime.delta(seconds=10): 
47:             target_price = get_target_price("BTC")
48:             mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
49:             ma5 = get_yesterday_ma5("BTC")
50:             sell_crypto_currency("BTC")
51:     
52:         current_price = pybithumb.get_current_price("BTC")        
53:         if (current_price > target_price) and (current_price > ma5):
54:             buy_crypto_currency("BTC")        
55:     except:
56:         print("에러 발생")        
57:     time.sleep(1)