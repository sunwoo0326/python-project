34: while True:
35:     now = datetime.datetime.now()
36:     if mid < now < mid + datetime.delta(seconds=10): 
37:         target_price = get_target_price(“BTC”)
38:         mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
39:         sell_crypto_currency("BTC")
40:
41:     current_price = pybithumb.get_current_price("BTC")
42:     if current_price > target_price:
43:         buy_crypto_currency("BTC")
44:
45:     time.sleep(1)