from pykrx import stock 

tickers = stock.get_market_ticker_list(market="KOSPI")
print(tickers[:10])