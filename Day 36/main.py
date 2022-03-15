import requests, itertools
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API = ""
NEWS_API = ""

yesterday_ = datetime.now() - timedelta(days = 1)
y_date = yesterday_.date()

stock_response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_API}")
stock_response.raise_for_status()
stock = stock_response.json()

news_response = requests.get(f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from={y_date}&sortBy=popularity&apiKey={NEWS_API}")
news_response.raise_for_status()
news = news_response.json()['articles']

# Iterate to get last two items from the dictionary
stock = dict(itertools.islice(stock['Time Series (Daily)'].items(), 0, 2))

closing = [float(stock[day]['4. close']) for day in stock]
differ = closing[0] / closing[1]
if differ > 1:
    differ = (differ - 1) * 100
    print(f"🔼 {STOCK} rose by {differ:.2}% yesterday")
else:
    differ = (1 - differ) * 100
    print(f"🔽 {STOCK} fell by {differ:.2}% yesterday")

print("----")
print(f"LATEST NEWS BY: {news[0]['source']['id'].upper()}")
print(news[0]['description'])
print(f"Source: {news[0]['url']}")