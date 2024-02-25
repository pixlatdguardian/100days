import requests
import datetime as dt

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": "apiKey"
}
datetime = dt.datetime.now()
three_days = datetime - dt.timedelta(days=3)
date = three_days.date()

news_params = {
    "from": date,
    "qInTitle": COMPANY_NAME,
    "apiKey": "apiKey"

}


## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def get_stocks():
    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    print(response.json())
    stock_prices = response.json()["Time Series (Daily)"]
    close_prices = []
    for date, daily_data in stock_prices.items():
        close_price = daily_data['4. close']
        close_prices.append(close_price)

    stock_diff = abs(float(close_prices[0]) - float(close_prices[1]))
    stock_percent = stock_diff / float(close_prices[0])

    if stock_percent > 0.05:
        news = requests.get(NEWS_ENDPOINT, params=news_params)
        articles = news.json()["articles"]
        top_articles = articles[:3]
        print(stock_percent)
        print([f"Headline: {article['title']}. \n Brief: {article['description']}" for article in top_articles])


get_stocks()
