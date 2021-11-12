import smtplib
import requests
import datetime as dt
from twilio.rest import Client

my_email = "abdikasymt@yahoo.com"
my_pass = "uscbserabegigjis"

account_sid = "AC67d6343e52156c4c0dc88ca85ca852ed"
auth_token = "3bc98b2c15d645dd491235eb45cb3591"

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API = "VW1OL8OXTC8GZPIL"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "cdcd0e789cb04c91971761716bad06e8"

now = dt.datetime.now()


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API
}

response_stocks = requests.get(url=STOCK_ENDPOINT, params=stock_params)
daily_stocks = response_stocks.json()["Time Series (Daily)"]


try:
    yesterday = now.date() - dt.timedelta(days=1)
    before_yesterday = now.date() - dt.timedelta(days=2)
    yesterday_close = float(daily_stocks[f"{yesterday}"]["4. close"])
except KeyError:
    yesterday = now.date() - dt.timedelta(days=2)
    before_yesterday = now.date() - dt.timedelta(days=3)
    yesterday_close = float(daily_stocks[f"{yesterday}"]["4. close"])

before_yesterday_close = float(daily_stocks[f"{before_yesterday}"]["4. close"])

difference = yesterday_close - before_yesterday_close
percentage_change = int(difference * 100 / yesterday_close)

if percentage_change > 0:
    symbol = "🔺"
else:
    symbol = "🔻"

total_change = f"{symbol}{abs(percentage_change)}%"


def get_news():
    if abs(difference) > float(yesterday_close) * 0.05:
        return True
    else:
        print("No significant change.")


if get_news():
    news_params = {
        "apiKey": NEWS_API,
        "q": f"{COMPANY_NAME}",
        "from": "2021-11-08",
        "to": "2021-11-10",

    }
    response_news = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news = response_news.json()["articles"][:3]

    message = [f"TSLA: {total_change}. \n{article['title']}. \n{article['description']}\n\n" for article in news]

    client = Client(account_sid, auth_token)
    for i in message:
        message = client.messages.create(
            body=i,
            from_="+17164669165",
            to="+77472600188"
        )

