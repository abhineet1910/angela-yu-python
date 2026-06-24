import random
from random import randint
import os
from dotenv import load_dotenv
import requests
from requests import Response

import requests_cache
from twilio.rest import Client
session = requests_cache.CachedSession(
    "stock_cache",
    expire_after=3600
)



STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
load_dotenv()
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
## STEP 1: Use https://newsapi.org/docs/endpoints/everything

apikey = os.getenv("ALPHA_API_KEY")
url = "https://www.alphavantage.co/query?"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": apikey
}
def get_stckprice():
    try:
        response = session.get(url=STOCK_ENDPOINT, params=parameters)
        response.raise_for_status()
        data = response.json()["Time Series (Daily)"]
    except requests.exceptions.RequestException as e:
        print(f"Network/API error fetching stock price: {e}")
        return None, None
    except KeyError:
        print("Unexpected response format — 'Time Series (Daily)' not found.")
        return None, None
    data_list = [value for (key, value) in data.items()]
    # print(data_list)
    try:
        yesterday_closing = float(data_list[0]["4. close"])
        daybefore_yes = float(data_list[1]["4. close"])
    except (IndexError, KeyError, ValueError) as e:
        print(f"Error parsing stock data: {e}")
        return None, None

    difference = yesterday_closing - daybefore_yes
    diff_percen = (difference / yesterday_closing) * 100
    return difference.__round__(2), diff_percen.__round__(2)



        # content = get_news()
        # print(content)


# When STurl = https://www.alphavantage.co/query?OCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
new_api_key = os.getenv("NEWS_API_KEY")
news_parameters={
    "apiKey": new_api_key,
    "q":COMPANY_NAME,
    "from":"2026-06-01",
    "sortBy":"popularity",
    "language":"en"
}
def get_news():
    articles = []
    try:
        response = session.get(url=NEWS_ENDPOINT, params=news_parameters)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network/API error fetching news: {e}")
        return None, None

    for article in data["articles"][:3]:
        title = (article["title"])
        disp = (article["description"])
        articles.append({"title": title,
            "description": disp,})
    return articles
news  = get_news()
difference,diff = get_stckprice()
# articles = get_news()
# print(articles)
# title = ((articles[0][0]))
# disp = (articles[0][1])
y = (f"the percentage difference is {diff}%")
up_down = None
if abs(diff) > 2:
    if difference > 0:
        up_down = "🔺"
    else:
        up_down = "🔻"

    # print(news)

    print(f"the difference between the yesterday stock and day before stock price is {difference}{up_down} and {diff}%")
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"tesla {difference}{up_down} by {diff}% from yesterday. "
                 f"Headline: {news[random.randint(0, len(news) - 1)] if news else 'No news available'}",
            from_="+17752694980",
            to="+918770769388",
        )
        print(message.sid)
        print(message.status)
    except Exception as e:
        print(f"Failed to send SMS via Twilio: {e}")








## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

