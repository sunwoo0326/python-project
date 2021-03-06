 while True:
     now = datetime.datetime.now()
     if mid < now < mid + datetime.delta(seconds=10): 
         target_price = get_target_price(“BTC”)
         mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
 
     current_price = pybithumb.get_current_price("BTC")
     if current_price > target_price:
         krw = bithumb.get_balance("BTC")[2]
         orderbook = pybithumb.get_orderbook("BTC")
         sell_price = orderbook['asks'][0]['price']  
         unit = krw/float(sell_price)
         bithumb.buy_market_order("BTC", unit)

        time.sleep(1)