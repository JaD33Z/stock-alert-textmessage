import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "YOUR NEWS API KEY"
STOCK_API_KEY = "YOUR STOCK API KEY"

#TODO 1. - Get yesterday's closing stock price. perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_params,)

#TODO 2. - Get the day before yesterday's closing stock price

data_daily = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data_daily.items()]
yesterday_close = data_list[0]["4. close"]
day_before_close = data_list[1]["4. close"]

#TODO 3. - positive difference between both days, the icons will be in the text message
up_down = None

pos_diff = (float(yesterday_close) - float(day_before_close))
if pos_diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percentage_diff = round((pos_diff / float(yesterday_close)) * 100)


#TODO 5. -  use the News API to get articles related to the COMPANY_NAME.

if abs(percentage_diff) > 1:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }
    news_data = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_articles = news_data.json()["articles"]

#TODO 6. - Use Python slice operator to create a list that contains the first 3 articles.

    recent_articles = news_articles[:3]

#TODO 7. - Create a new list of the first 3 article's headline and description

    first_3_articles = [f"{STOCK_NAME} {up_down} %{percentage_diff} \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in recent_articles]
    print(first_3_articles)

#TODO 10. - Send each article as a separate message via Twilio.

    account_sid = YOUR-TWILIO-ID
    auth_token = YOUR-TWLIO-TOKEN
    twil_phone = YOUR-GIVEN-TWILIO-NUMBER
    client = Client(account_sid, auth_token)

    for article in first_3_articles:
        message = client.messages \
            .create(
            body= article,
            from_= twil_phone,
            to='+1YOURPHONENUMBER'
        )
